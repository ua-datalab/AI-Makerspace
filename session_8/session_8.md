## Some useful AI tools
**For tracking your AI model training or fine tuning progression etc**
- [MLFlow](https://mlflow.org/)
- [Wandb](https://wandb.ai/home)

**Hosted AI providers**
- [VLLM](https://github.com/vllm-project/vllm)
- - used for complex work loads, high-throughput and low-latency inference
- [LiteLLM](https://docs.litellm.ai/docs/)
- - lite weight and simpler usecases
- [web interface Hosted](https://openwebui.com/)
- [Chatbox](<https://github.com/Bin-Huang/chatbox/>)
- - Store data locally/private and talk to an AI
- [Anythigai](https://docs.anythingllm.com/)
- Paid + On Demand
- - OpenAI API(https://openai.com/api/)
  - [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- Paid + Serverless
- - [AWS Lambda](https://aws.amazon.com/lambda/) 

**Tracking and optimization and debugging of your LLM hosting and usage**

- [Lunary](https://lunary.ai/)
- -  Tracks API usage
- [Langfuse](https://github.com/langfuse/langfuse)
- - Workflow debugging
- - Visual time lines
- [Helicone](https://www.helicone.ai/)
    - - tracking, optimizing, and debugging API usage
- [Promptlayer](https://www.promptlayer.com/)
- - Prompt management
- - Version control for prompts
- - Prompt analytics
- [Traceloop](https://www.traceloop.com/)
- - real-time tracing, debugging, and monitoring
- [LangSmith](https://www.langchain.com/langsmith)
- - Wrapper for Langchain
         
**Some interesting applications already out there for llm**
- *Code for me*
- - [Openhands](https://docs.all-hands.dev/modules/usage/getting-started)
  - Please write a bash script hello.sh that prints "hello world!"
- *Write and evaluate grant applications for me*
- - [Grantasuarus](https://sc.edu/about/offices_and_divisions/research/news_and_pubs/news/2024/20241009_AI_Roadmap_Launch.php)
- *simulate realistic human-like behaviors in programmatically defined environments.*
- - [Troupe](https://github.com/microsoft/TinyTroupe)
- *Help with real life problems/break down*.  
- - [Fabric](https://github.com/danielmiessler/fabric)
               

- *Web Crawlers with AI.*
- - [Crawl4ai](https://github.com/unclecode/crawl4ai)
- - [Ivy](https://ivy.ai/ai-web-crawler)

- *Upload your own data and query it*
- - [notebookLM](https://notebooklm.google.com/?authuser=1&original_referer=https:%2F%2Fduckduckgo.com%23)

- Identify ai generated content*
    - [Synthid](https://deepmind.google/technologies/synthid/)
- [AI Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

- **Online Classes for AI** 
- - [Fast Ai](https://www.fast.ai/)
- - [Khan Academy](https://www.khanacademy.org)
- - - helps you learn with Khanmingo bot

**Lightweight/edge/On device models**
- [Smolllm](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct)
- [Llmware](https://llmware.ai/)
- - Financial legal compliance
- [Torchao- Pytorch tool to reduce size of llm](https://pytorch.org/blog/pytorch-native-architecture-optimization/)
- [Review paper on other small language models](https://arxiv.org/abs/2409.15790)
- [Tiny agent from Berkeley](https://huggingface.co/squeeze-ai-lab/TinyAgent-ToolRAG)
- [NVIDIA’s nemotron](https://www.marktechpost.com/2024/09/14/nvidia-open-sources-nemotron-mini-4b-instruct-a-4096-token-capacity-small-language-model-designed-for-roleplaying-function-calling-and-efficient-on-device-deployment-with-32-attention-heads-and-9/)
- [Yicoder](https://github.com/01-ai/Yi-Coder)

**University related AI platforms**
- [AI Verde](https://chat.openai.com/)
- - University of Arizona's free serverless Providers
  - Built on cyverse and NSF Jetstream
- [Maizey](https://www.youtube.com/watch?v=Lkyy1cvQiKA)
- - U Michigan
- [anvil gpt](https://www.rcac.purdue.edu/knowledge/anvil/anvilgpt)
- - Purdue + ACCESS + NSF Jetstream

**Biology/Medicine related**


**1. BioGPT**
- **Description**: Developed by Microsoft Research, BioGPT is a transformer-based model fine-tuned on biomedical literature. It excels in extracting relationships between biomedical entities and answering domain-specific questions.
- **Applications**:
  - Mining relationships in biomedical datasets.
  - Extracting structured data from clinical notes and scientific papers.
- **Access**: Available on [Hugging Face](https://huggingface.co/microsoft/BioGPT).

---

**2. ClinicalBERT**
- **Description**: ClinicalBERT is a fine-tuned version of BERT on clinical text, particularly from the MIMIC-III dataset. It is designed to process EHR data effectively.
- **Applications**:
  - Clinical note analysis.
  - Predicting medical outcomes and improving patient care.
- **Strength**: Tailored for natural language processing (NLP) tasks specific to healthcare.

---

**3. MedPaLM and MedPaLM 2**
- **Description**: MedPaLM is an adaptation of Google's PaLM, fine-tuned on medical datasets to handle health-related queries and extract actionable insights from patient data.
- **Applications**:
  - Conversational agents for healthcare.
  - Summarizing clinical documents.
- **Advancement**: Designed to meet medical safety and accuracy standards.

---

**4. PubMedGPT**
- **Description**: PubMedGPT is trained on the PubMed database, a vast repository of biomedical literature. It focuses on extracting and generating insights related to biomedical research.
- **Applications**:
  - Literature review automation.
  - Drug interaction studies.
- **Strength**: Specialized for handling biomedical research content.

---

**5. BioBERT**
- **Description**: BioBERT is a BERT-based model trained on PubMed abstracts and PubMed Central full-text articles. It is one of the first models tailored for biomedical text mining.
- **Applications**:
  - Named entity recognition (NER) for biomedical terms.
  - Relationship extraction in biomedical research.
- **Access**: Freely available for research purposes.

---

**6. Galactica**
- **Description**: Meta AI's Galactica is designed for scientific knowledge representation, including biomedical contexts.
- **Applications**:
  - Summarizing scientific articles.
  - Extracting structured information from unstructured text.
- **Strength**: Multidisciplinary but includes a strong focus on biomedical data.

---

**7. SapBERT**
- **Description**: SapBERT (Self-Aligned BERT) focuses on biomedical concept representation and entity normalization.
- **Applications**:
  - Linking biomedical concepts in databases.
  - Structured information extraction.
- **Special Feature**: Performs exceptionally well in cross-lingual medical text processing.

---

**8. MedAlpaca and Pythia (Healthcare Variants)**
- **Description**: Fine-tuned versions of Alpaca or Pythia models optimized for healthcare settings.
- **Applications**:
  - Medical transcription and summarization.
  - Diagnosis assistance through structured text processing.
- **Strength**: Tuned for rapid deployment in healthcare workflows.

---

 **9. ClinicalTransformer Models**
- **Description**: A family of transformer-based models specifically designed for healthcare providers and researchers to automate clinical document processing.
- **Applications**:
  - Extracting ICD (International Classification of Diseases) codes from clinical notes.
  - Analyzing diagnostic imaging reports.

---
 **10. Custom Models by Large Companies**
- Many tech companies are developing proprietary models or fine-tuning open-source ones for medical use:
  - **IBM Watson Health NLP**: Focuses on cancer care and clinical trials.
  - **Microsoft Azure Health Bot**: Analyzes patient conversations and extracts relevant data.
  - **Amazon HealthLake NLP**: Processes and extracts insights from EHRs.
- **11** [curateGPT](https://github.com/monarch-initiative/curategpt?tab=readme-ov-file)
- **12** [mCodeGPT](https://mcodegpt.org/)
- - for extracting Minimal Common Oncology Data Elements (mCODE) from EHRs.
- **13** [SDoH-GPT](https://github.com/AIM-Harvard/SDoH)
  - for extracting Social Determinants of Health (SDoH) from unstructured data in EHRs

---
**Knowledge curation related**
- [Stanford's storm](https://storm.genie.stanford.edu/)
- - Write wikipedia like articles
- [Labelbox](https://docs.labelbox.com/)
- - data annotation platform


**News**
- [Best open source AI models (as of Nov 2024)](https://www.zdnet.com/article/the-best-open-source-ai-models-all-your-free-to-use-options-explained/)
- [AI For visually impaired](https://www.hackster.io/shahizat/ai-powered-application-for-the-blind-and-visually-impaired-df3f9e)
- [Turn by turn access with AI For visually impaired](https://arxiv.org/html/2410.19954v1)
- [VIASSIST For visually impaired](https://arxiv.org/html/2404.02508v1)
- [LLmflation Keeping track of LLM Costs](https://a16z.com/llmflation-llm-inference-cost/)
- [Economics of Hosting open source llms](https://towardsdatascience.com/economics-of-hosting-open-source-llms-17b4ec4e7691)

