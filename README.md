# py-env

> A simple, flexible Python starter kit for working with LLMs using Conda + Ollama or OpenAI.

A portable, reproducible Python environment for working with LLMs (Large Language Models) using both local and cloud-based providers like **Ollama** and **OpenAI**.

---

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vedanta/py-env/HEAD?labpath=llm_demo.ipynb)

## 📦 Features

* ✅ Environment setup using Conda + pip
* ✅ LLMClient abstraction for Ollama and OpenAI
* ✅ .env-based configuration for flexible model switching
* ✅ Includes testing script and interactive Jupyter notebook
* ✅ Clean folder structure with starter files for collaboration
* ✅ Supports streaming JSON responses from Ollama

---

## 🚫 Binder Limitations

Binder currently **does not support Ollama**, which is required to run this project locally with models like `orca-mini`.

As a result, while the notebook may launch, it will not produce valid LLM responses unless reconfigured to use OpenAI with a valid API key.

> ✅ To run this project fully, clone the repo and follow the local setup instructions below.

---

## 🛠️ Setup Guide

To run locally:

### 1. Clone or Download

Clone the repository or download the ZIP and extract it:

```bash
git clone <your-repo-url>
cd py-env
```

---

### 2. Create the Conda Environment

To set a custom name for your environment, edit the `name:` field in `environment.yml` before running the command. Example:

```yaml
name: my-custom-env
```

Then create the environment:

```bash
conda env create -f environment.yml
conda activate py-env
```

> 💡 To update the environment later (e.g., after adding new packages):
>
> ```bash
> pip install <new-package>
> pip freeze > requirements.txt
> conda env update -f environment.yml --prune
> ```

---

### 3. Configure Environment Variables

Copy the sample environment configuration:

```bash
cp .env.sample .env
```

Edit `.env` to choose which LLM backend you want to use:

#### For **Ollama + Orca-Mini**:

```dotenv
USE_OLLAMA=true
OLLAMA_MODEL=orca-mini
USE_OPENAI=false
```

Ensure Ollama is installed and running: [https://ollama.com](https://ollama.com)

#### For **OpenAI (e.g. GPT-4)**:

```dotenv
USE_OLLAMA=false
USE_OPENAI=true
OPENAI_API_KEY=sk-<your-key>
OPENAI_MODEL=gpt-4
```

> 🔐 Never commit `.env` with real API keys to Git.

---

### 4. Run a Test

This script calls the LLM using your `.env` settings:

```bash
python test_client.py
```

Expected output:

```
LLM Response:
 <generated response here>
```

---

### 5. Use the Notebook

A notebook (`llm_demo.ipynb`) is included for interactive exploration:

```bash
jupyter notebook llm_demo.ipynb
```

* Cell 1: Instantiates the LLM client from `.env`
* Cell 2: Sends a test prompt and displays response

---

## 📁 Folder Structure

Includes Binder setup for zero-install cloud execution:

```
py-env/
├── .binder/             # Binder environment and build scripts
│   ├── environment.yml
│   └── postBuild
├── .env.sample         # Template for environment variables
├── .env.minimal        # Minimal config for Ollama-only use
├── .gitignore          # Files and folders to exclude from Git
├── environment.yml     # Conda + pip environment definition
├── llm_client.py       # Reusable class for OpenAI + Ollama
├── llm_demo.ipynb      # Jupyter notebook demo
├── requirements.txt    # pip dependencies
├── setup_env.sh        # Shell script to automate setup
├── test_client.py      # Basic test script to verify LLM use
```

---

## 🔍 Notes

* `llm_client.py` auto-loads `.env` and handles JSON streaming from Ollama
* Lazy import of `openai` prevents crash if not installed
* Use `.env.minimal` if you're only using Ollama locally
* Jupyter-friendly design makes it easy to test and iterate
* All defaults are safe and extensible

---

## 🔁 Extending the Project

* ✅ Add new prompts in `test_client.py` or the notebook
* ✅ Build a CLI around `LLMClient`
* ✅ Deploy as an API using FastAPI or Flask
* ✅ Add more `.env` configs for Azure/OpenRouter/etc.

---

## 🪪 License

MIT or your preferred license. Attribution appreciated if forked or reused.
