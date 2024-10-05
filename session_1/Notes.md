# Distributed Training using PyTorch

## Prerequisites
- An HPC account
- Download ImageNet on the HPC
## Motivation
Often, we train models that are too large to fit on a single GPU, such as LLMs. Our campus has HPC facilities in which we have access to nodes with GPUs themselves, however, given the sheer size of today’s models and datasets, we can benefit from doing multimode training.
Today we are going to focus on adapting PyTorch code to run in a multimode environment, to speed up training. We will test Resnet50, a stacked CNN for image classification and let it run for one epoch on imagenet

## Links
- ResNet50 training [blog post](https://moiseevigor.github.io/software/2022/12/18/one-pager-training-resnet-on-imagenet/)
- ImageNet 1k [Kaggle dataset](https://www.kaggle.com/competitions/imagenet-object-localization-challenge/data)
- UofA's [HPC documentation](https://hpcdocs.hpc.arizona.edu/)
- [Writing distributed apps with PyTorch](https://pytorch.org/tutorials/intermediate/dist_tuto.html)
- Distributed Data Parallel [example](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html)
 

