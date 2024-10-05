import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision
import torchvision.transforms as transforms

import torch.multiprocessing as mp
from torch.utils.data.distributed import DistributedSampler
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.distributed import init_process_group, destroy_process_group
from tqdm import tqdm
import os


def ddp_setup(rank, world_size):
    """
    Args:
        rank: Unique identifier of each process
        world_size: Total number of processes
    """
    #os.environ["MASTER_ADDR"] = os.environ["SLURM_JOB_NODELIST"].split(",")[0] + ".puma.hpc.arizona.edu"
    #print(os.environ["MASTER_ADDR"])
    #os.environ["MASTER_PORT"] = "12355"
    #torch.cuda.set_device(rank)
    #init_process_group(backend="nccl", rank=rank, world_size=world_size)
    init_process_group(backend="nccl")
    print("Boop")

class Trainer:
    def __init__(
        self,
        model: torch.nn.Module,
        train_data: DataLoader,
        optimizer: torch.optim.Optimizer,
        gpu_id: int,
        save_every: int,
    ) -> None:
        self.gpu_id = gpu_id
        self.model = model.to(gpu_id)
        self.train_data = train_data
        self.optimizer = optimizer
        self.save_every = save_every
        self.model = DDP(model, device_ids=[gpu_id])

    def _run_batch(self, source, targets):
        self.optimizer.zero_grad()
        output = self.model(source)
        loss = F.cross_entropy(output, targets)
        loss.backward()
        self.optimizer.step()

    def _run_epoch(self, epoch):
        b_sz = len(next(iter(self.train_data))[0])
        print(f"[GPU{self.gpu_id}] Epoch {epoch} | Batchsize: {b_sz} | Steps: {len(self.train_data)}")
        self.train_data.sampler.set_epoch(epoch)
        loader = tqdm(self.train_data, desc="Step") if self.gpu_id == 0 else self.train_data
        for source, targets in loader:
            source = source.to(self.gpu_id)
            targets = targets.to(self.gpu_id)
            self._run_batch(source, targets)

    def _save_checkpoint(self, epoch):
        ckp = self.model.module.state_dict()
        PATH = "checkpoint.pt"
        torch.save(ckp, PATH)
        print(f"Epoch {epoch} | Training checkpoint saved at {PATH}")

    def train(self, max_epochs: int):
        for epoch in range(max_epochs):
            self._run_epoch(epoch)
            if self.gpu_id == 0 and epoch % self.save_every == 0:
                self._save_checkpoint(epoch)


def load_train_objs():
    # Load the ResNet50 model
    model = torchvision.models.resnet50(pretrained=True)
    learning_rate = 0.001
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    return model, optimizer


def prepare_dataloader(batch_size: int):
    path = '/xdisk/enoriega/enoriega/IMAGENET/ILSVRC/Data/CLS-LOC/train'

    # Load the ImageNet Object Localization Challenge dataset

    # Initialize transformations for data augmentation
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomRotation(degrees=45),
        transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    train_dataset = torchvision.datasets.ImageFolder(
        root=path, 
        transform=transform
    )
    return DataLoader(
        train_dataset,
        batch_size=batch_size,
        pin_memory=True,
        shuffle=False,
        num_workers=8,
        sampler=DistributedSampler(train_dataset)
    )


def main(rank: int, world_size: int, save_every: int, total_epochs: int, batch_size: int):


    # create model and move it to GPU with id rank
    device_id = rank % torch.cuda.device_count()

    ddp_setup(rank, world_size)
    model, optimizer = load_train_objs()
    train_data = prepare_dataloader(batch_size)
    trainer = Trainer(model, train_data, optimizer, rank, save_every)
    trainer.train(total_epochs)
    destroy_process_group()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='simple distributed training job')
    parser.add_argument('total_epochs', type=int, help='Total epochs to train the model')
    parser.add_argument('save_every', type=int, help='How often to save a snapshot')
    parser.add_argument('--batch_size', default=32, type=int, help='Input batch size on each device (default: 32)')
    args = parser.parse_args()

    world_size = 2
    #rank = int(os.environ["SLURM_ARRAY_TASK_ID"]) - int(os.environ["SLURM_ARRAY_TASK_MIN"])
    mp.spawn(main, args=(world_size, args.save_every, args.total_epochs, args.batch_size), nprocs=1)
