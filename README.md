# Adaptive Tokenization for Arabic Language: Unpacking Strategies for Low-Resource NLP

This repository presents the implementation and analysis developed for our COMP0087 Statistical Natural Language Processing group project at University College London, titled:

**"Evaluating Dynamic Tokenization Strategies in Low-Resource Languages: A Case Study on Arabic"**

The project explores how different tokenization paradigms - including static, dynamic, and embedding-extended approaches - affect performance in low-resource natural language processing (NLP) tasks. Our experiments focus on Arabic, using stance classification and extractive question answering benchmarks, and fine-tune open large language models (LLMs) such as LLaMA 3.1 and Gemma 7B.

## Abstract

Tokenization is a foundational step in NLP pipelines, yet most existing tokenizers are optimized for high-resource languages. This study investigates the limitations of static subword tokenizers when applied to morphologically rich, underrepresented languages such as Arabic. We present a comparative evaluation of static tokenization, dynamic pair-merging, and embedding-aware vocabulary extensions. Our empirical findings demonstrate that even lightweight adjustments to token boundaries can lead to measurable improvements in model performance and significantly reduce out-of-vocabulary (OOV) rates - offering a pathway toward more inclusive and efficient language modeling in low-resource settings.

## Selected Datasets

- **AraStance**: A stance detection dataset of Arabic tweets, annotated with Favor, Against, or Neutral labels  
  https://github.com/Tariq60/arastance

- **ArabicQA**: A large-scale dataset for extractive question answering in Modern Standard Arabic and dialects  
  https://github.com/DataScienceUIBK/ArabicaQA

## Quickstart

### Installation

To set up the environment locally:

```bash
git clone https://github.com/MeriemMhr/unpacking-adaptive-tokenization-strategies-arabic-nlp.git
cd unpacking-adaptive-tokenization-strategies-arabic-nlp

# (Recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Note: All experiments were executed on Google Colab, with support for both CPU and A100 GPU runtimes. Access to the Hugging Face Hub is required (`huggingface-cli login`), and Google Drive should be mounted for dataset access.

### Experiment Navigation

Our experiments are organized into three main folders under the [`experiments/`](./experiments) directory for easier navigation and reproducibility:

- [`question-answering/`](./experiments/question-answering): contains experiments evaluating tokenization strategies on Arabic and Estonian QA datasets.  
- [`stance-detection-classification/`](./experiments/stance-detection-classification): includes stance classification tasks across multiple languages and model variants.
- [`dynamic-tokenization/`](./experiments/dynamic-tokenization): explores adaptive token selection strategies.

Each folder contains self-contained notebooks with relevant implementation details, training logs, and evaluation visualizations.

## Tokenization Metrics

The following metrics are tracked across experiments:

- **Token Fertility** (tokens per character)
- **Token Length** (mean and median)
- **Compression Ratio** (characters per token)
- **Vocabulary Usage** (% of vocab utilized)
- **Out-of-Vocabulary Rate** (OOV)

These indicators provide insights into how well a tokenizer handles morphologically complex text and are visualized throughout the project notebooks.

## Project Context

This project was developed as part of the [COMP0087: Statistical Natural Language Processing](https://comp0087.cs.ucl.ac.uk/) module at UCL (2024/25). It contributes to the broader research discourse on adaptive tokenization techniques, multilingual modeling, and equitable language technology for underrepresented linguistic communities.

To access our final paper, see: **[View the full report (.pdf)](https://placeholder-link.com/tokenization-paper)**

## Citation

If you use or refer to this work, please cite:

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

We gratefully acknowledge **Professor Pontus Stenetorp** for leading the COMP0087 module and cultivating a research-driven learning environment. Special thanks to **Eduardo Sánchez**, our teaching assistant, for his insightful feedback and support throughout the development of this project.

## Contact

For questions, contributions, or academic correspondence:  
**Meriem Mehri** - https://github.com/MeriemMhr | meriem.mehri.24@ucl.ac.uk
