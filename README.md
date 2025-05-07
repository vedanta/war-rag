# py-env

A portable, reproducible Python environment using Conda and pip. This setup is ideal for data science, machine learning, and LLM projects.

---

## 🔧 Environment Setup

This project uses **Conda** for environment management and **pip** for Python packages.

### 📦 Requirements

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Git

---

## 🚀 Create the Environment

```bash
conda env create -f environment.yml
conda activate py-env
```

This will:
- Create a new Conda environment named `py-env`
- Install Python 3.10 and pip
- Install all pip packages listed in `requirements.txt`

---

## 📁 Project Structure

```bash
.
├── environment.yml       # Conda environment file (with pip section)
├── requirements.txt      # Pip dependencies
├── .gitignore            # Files ignored by Git
└── README.md             # This file
```

---

## 🔄 Updating Dependencies

To add new packages:

```bash
# Inside the environment
pip install new-package
pip freeze > requirements.txt
```

To update the environment:

```bash
conda env update -f environment.yml --prune
```

---

## 📚 Tips

- Always use `pip freeze > requirements.txt` after installing pip packages.
- Use `conda env export --from-history > environment.yml` to capture minimal dependencies.
- Avoid committing the `prefix:` key in your `environment.yml`.

---

## ✅ License

MIT or your preferred license.
