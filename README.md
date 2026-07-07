# Python for AI 🐍🤖

A beginner-friendly, week-by-week **Python course built for aspiring Agentic AI Engineers**. Each week teaches core Python concepts through live-class notes (in **Hinglish** — explanations in Hindi/English, all code and terms in English) plus runnable `.py` scripts and Jupyter notebooks.

Every topic is tied back to one goal: **understanding how real AI agents are built** (they think, use tools, and loop — and it's all Python underneath).

---

## Who is this for?

- Complete beginners who have never written code.
- Learners who want a **job-ready, industry-style setup** from day one (Cursor, `uv`, Git, GitHub).
- Anyone aiming to become an **Agentic AI Engineer**.

---

## Prerequisites

- **Python 3.13+** (course narration targets the latest Python 3.x)
- A code editor — **[Cursor](https://cursor.com/download)** or [VS Code](https://code.visualstudio.com/)
- **[uv](https://docs.astral.sh/uv/)** — fast Python environment & package manager
- **Git** + a **GitHub** account

> No laptop? Week 0 shows you how to start on **Google Colab** with just a browser.

---

## Getting started

Clone the repo and set up the environment with `uv`:

```bash
git clone https://github.com/IndianAIProduction/python_for_ai.git
cd python_for_ai
uv sync
```

Run a script:

```bash
uv run week00_setup_first_run/first_program.py
```

Open a notebook (`.ipynb`) directly in Cursor / VS Code and select the Python 3.13 kernel, or launch Jupyter:

```bash
uv run jupyter notebook
```

---

## Course structure

| Week | Folder | Topics |
|------|--------|--------|
| **Week 0** | [`week00_setup_first_run/`](week00_setup_first_run/) | What is programming & AI agents, Google Colab, installing Python + Cursor, the terminal, REPL vs `.py` files, Jupyter notebooks, reading errors calmly, `uv`, Git, GitHub |
| **Week 1** | [`week01_data_variables/`](week01_data_variables/) | Variables, numbers & arithmetic, strings & f-strings, booleans, types & type conversion, `input()`, string methods, mini projects |
| **Week 2** | [`week02_decision_and_repitition/`](week02_decision_and_repitition/) | `if`/`elif`/`else` & truthiness, nested conditions & ternary, `for` loops & `range`, `while` loops & loop control, nested loops & `match`/`case`, mini projects |

Each week folder contains:

- A **`Week-XX_*.md`** file — the full live-class notes (concepts, definitions, demos, homework).
- A **`code/`** folder and/or standalone scripts/notebooks — the runnable examples and projects.

---

## Highlighted projects

- **Temperature Converter** — Celsius → Fahrenheit (`week01_data_variables/temperature_convertor.py`)
- **AI Token-Cost Estimator** — estimate the cost of AI model tokens (`week01_data_variables/token_cost_enstimator.py`)
- **Grade Checker** — `if`/`elif`/`else` practice (`week02_decision_and_repitition/code/check_grade.py`)
- **Menu Calculator** & **Number Guessing Game** — see Week 2 notes

---

## How to use this course

1. Read the week's `Week-XX_*.md` notes top to bottom.
2. Type out every code block yourself — don't copy-paste.
3. Do the **Homework** and the **weekend revision task** at the end of each week.
4. Commit your work with Git and push it to GitHub to build your portfolio.

---

## Repository layout

```
python_for_ai/
├── week00_setup_first_run/       # Setup, first programs, tooling
├── week01_data_variables/        # Data types, variables, I/O
├── week02_decision_and_repitition/  # Conditionals & loops
├── pyproject.toml                # Project metadata & dependencies
├── uv.lock                       # Locked dependency versions
└── README.md
```

---

Happy learning — and welcome to your journey toward becoming an **Agentic AI Engineer**! 🚀

