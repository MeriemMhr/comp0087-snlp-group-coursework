# COMP0087: Evaluating Dynamic Tokenization Strategies in Low Resource Languages

This repository contains the implementation and analysis for our COMP0087 Statistical Natural Language Processing group project at UCL, titled:

**“Evaluating Dynamic Tokenization Strategies in Low-Resource Languages: A Case Study on Arabic”**

This work explores how different tokenization paradigms — static, dynamic, and embedding-extended — impact performance in low-resource NLP settings, with a specific focus on Arabic. The project benchmarks multiple strategies using stance classification and extractive question answering tasks on AraStance and ArabicQA datasets, fine-tuned on open LLMs like LLaMA 3.1 and Gemma 7B.

## Abstract

Tokenization is a fundamental component in NLP pipelines, yet most tokenizers are optimized for high-resource languages. This project investigates the limitations of such static tokenizers when applied to morphologically rich and underrepresented languages like Arabic. We propose a comparative evaluation between static subword tokenization, dynamic token merging, and embedding-aware vocabulary extensions. Our empirical results demonstrate that even lightweight token-level modifications can substantially improve downstream performance and reduce out-of-vocabulary (OOV) rates — setting new baselines for efficient and inclusive tokenization in low-resource language processing.

## Selected Datasets

- **AraStance**: A stance detection dataset of Arabic tweets labeled as Favor, Against, or Neutral  
  https://github.com/Tariq60/arastance

- **ArabicQA**: A large-scale question-answering dataset for Modern Standard Arabic and dialects  
  https://github.com/DataScienceUIBK/ArabicaQA

## Quickstart

### Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/MeriemMhr/unpacking-adaptive-tokenization-strategies-arabic-nlp.git
cd unpacking-adaptive-tokenization-strategies-arabic-nlp

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

Note: All experiments were run on Google Colab with CPU or A100 GPU fallback. Ensure access to Hugging Face Hub (`huggingface-cli login`) and mount Google Drive to access large datasets.

### Running the Experiments

#### 1. Static Tokenization Baseline (LLaMA and Gemma)
Notebooks:
- `notebooks/stance_classification_static.ipynb`
- `notebooks/qa_evaluation_static.ipynb`

#### 2. Tokenizer Extension (Embedding-Aware)
Notebook:
- `notebooks/tokenizer_extension_embedding_aware.ipynb`

Includes evaluation of:
- Token fertility
- Compression ratio
- Vocabulary usage
- OOV rate

#### 3. Dynamic Tokenization Integration
Notebook:
- `notebooks/dynamic_tokenization_pooling.ipynb`

Based on external library:  
https://github.com/PiotrNawrot/dynamic-pooling

Each notebook includes evaluation plots, training logs, and metric tables.

## Tokenization Metrics

We report and visualize the following:

- Token Fertility (tokens per character)
- Mean and Median Token Length
- Compression Ratio (characters per token)
- Vocabulary Usage (% of vocab used)
- Out-of-Vocabulary (OOV) Rate

These metrics are reported per model and tokenizer setup and can be found in the results section of each notebook.

## Project Context

This project was developed as part of the [COMP0087: Statistical Natural Language Processing](https://comp0087.cs.ucl.ac.uk/) module at University College London (2024/25). It aims to contribute to the growing research on fair, efficient, and linguistically informed NLP techniques — particularly within low-resource language contexts such as Arabic.

## Citation

If you use or reference this work, please cite it as:

```
@misc{adaptive-tokenization-arabic-2025,
  title={Evaluating Dynamic Tokenization Strategies in Low-Resource Languages},
  author={Meriem Mehri et al.},
  year={2025},
  note={UCL COMP0087 Group Project},
  howpublished={\url{https://github.com/MeriemMhr/unpacking-adaptive-tokenization-strategies-arabic-nlp}}
}
```

## Acknowledgments

We would like to thank Professor Pontus Stenetorp for leading the COMP0087 module and fostering a research-oriented environment that encourages both rigor and creativity in natural language processing.  
A special thanks to our teaching assistant, Eduardo Sánchez, whose guidance and feedback were invaluable throughout this project.

## Contact

For questions or collaborations, please contact:  
**Meriem Mehri** — https://github.com/MeriemMhr
