# NLP Deep Learning project

## Description

This project solves classification problem on [ag_news](https://huggingface.co/datasets/ag_news) dataset. Each text belongs to one class, four classes in total, **World, Sports, Business, Sci/Tech**.

- Decoder: GPT2, with custom classification head and frozen odd layers
- Encoder: RoBERTa, custom classification head and LoRA (PEFT method)
- Encoder-decoder: T5 with frozen all layers except last $n$ layers
- Prompting: FLAN-T5, as zero-shot

## How to run

Run `jupyterlab` installed in conda environment.

## Development
Follow the steps below to setup the development environment:

- For development, install the environment with the following command:
```bash
    conda env create -f environment.yml
```
- Activate the environment with the following command:
```bash
    conda activate nlp-dl
```
- Init pre-commit hooks with the following command:
```bash
    pre-commit install
```