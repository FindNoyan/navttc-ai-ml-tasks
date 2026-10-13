<!-- Task 01 — Installation Guide -->
<!-- Source: Annexure-I, AI_NAVTTC_Outline_Tasks.pdf -->
<!-- This file explains how to install the tools used in this course on Windows. -->
<!-- After following it, you can verify that Python, Anaconda, PyTorch, TensorFlow, VS Code and PyCharm are working. -->

# Task 01 — Installation Guide (Windows-first)

This guide installs everything needed for the NAVTTC AI/ML course (Batch 3 Morning, Netsol).
Follow the steps in order. After each install, run the **verify** command to confirm it works.

> Note: These are the tools listed in Annexure-I of the course outline:
> Anaconda3, PyTorch, TensorFlow 2.0, VS Code, PyCharm.

---

## Step 0 — Before you start

- You need a Windows 10 / Windows 11 computer with internet.
- You need about 5 GB of free disk space.
- If a step asks "Add to PATH", tick that box when it appears.

---

## Step 1 — Install Anaconda3 (includes Python + conda)

Anaconda gives us Python plus the `conda` package manager. We will use it for everything else.

1. Go to the official Anaconda download page: https://www.anaconda.com/download
2. Download **Anaconda Distribution** for Windows (64-bit, Python 3.x).
3. Run the downloaded `.exe` file.
4. Click **Next**, accept the licence, choose **Just Me**.
5. Keep the default install folder, e.g. `C:\Users\<YourName>\anaconda3`.
6. Tick **"Add Anaconda3 to my PATH environment variable"** if it appears, then click **Install**.
7. When finished, open a fresh **Anaconda Prompt** (search it in the Start menu).

**Verify Anaconda:**

```bash
conda --version
python --version
```

You should see a conda version (e.g. `conda 24.x.x`) and a Python version (e.g. `Python 3.11.x`).

---

## Step 2 — Install PyTorch

PyTorch is a deep-learning library. We install the CPU version, which works on any computer.

1. Open **Anaconda Prompt**.
2. (Recommended) Create a separate environment so packages do not clash:

```bash
conda create -n navttc python=3.11 -y
conda activate navttc
```

3. Install PyTorch (CPU-only build from the official PyTorch index):

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

**Verify PyTorch:**

```bash
python -c "import torch; print(torch.__version__)"
```

You should see a version number such as `2.x.x+cpu`.

---

## Step 3 — Install TensorFlow 2.0 (or newer 2.x)

TensorFlow is another deep-learning library used in this course.

1. In the same **Anaconda Prompt** (with the `navttc` environment active):

```bash
pip install tensorflow
```

2. Wait for the install to finish. It downloads a few extra packages — that is normal.

**Verify TensorFlow:**

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

You should see a version number starting with `2.` (e.g. `2.16.1`).

**Check both libraries together (optional):**

```bash
python -c "import torch, tensorflow as tf; print('PyTorch:', torch.__version__); print('TensorFlow:', tf.__version__)"
```

---

## Step 4 — Install VS Code

VS Code is a light, free code editor. We will write most Python programs in it.

1. Go to the official VS Code download page: https://code.visualstudio.com/Download
2. Download **Windows** (User Installer, 64-bit) and run the `.exe`.
3. During setup, tick these two boxes if they appear:
   - "Add to PATH"
   - "Register Code as an editor for supported file types"
4. Click **Install**, then **Finish**.
5. Open VS Code. Install the **Python extension** by Microsoft:
   - Click the Extensions icon on the left sidebar.
   - Search for `Python`, install the one by Microsoft.
6. Open any `.py` file. VS Code will ask which Python to use — pick the `navttc` environment (the one with Anaconda).

**Verify VS Code:**

```bash
code --version
```

You should see a VS Code version number.

---

## Step 5 — Install PyCharm

PyCharm is a full Python IDE (a bigger editor with more built-in tools).

1. Go to the official PyCharm download page: https://www.jetbrains.com/pycharm/download/
2. Download **PyCharm Community Edition** (free) for Windows.
3. Run the `.exe` and follow the installer. Keep the defaults.
4. On first launch, choose **New Project**, then set the interpreter to the `navttc` conda environment:
   - File → Settings → Project → Python Interpreter → Add Interpreter → Conda Environment → choose `navttc`.

**Verify PyCharm:**

Open PyCharm, create a new file called `test.py`, type:

```python
print("Hello, PyCharm!")
```

Run it (green ▶ button). It should print `Hello, PyCharm!`.

---

## Quick checklist — all verify commands in one place

Run these after all installs. Every command should print a version number or a message, not an error.

```bash
conda --version
python --version
python -c "import torch; print(torch.__version__)"
python -c "import tensorflow as tf; print(tf.__version__)"
code --version
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `'conda' is not recognized` | Close and reopen Anaconda Prompt (not normal cmd), or reinstall Anaconda with "Add to PATH" ticked. |
| `'python' is not recognized` | Same as above — use Anaconda Prompt, or add Python to PATH. |
| PyTorch / TensorFlow install is slow | Normal — they are large packages. Keep the internet connected and wait. |
| VS Code says "Python not found" | Install the Microsoft Python extension, then select the `navttc` interpreter (Ctrl+Shift+P → "Python: Select Interpreter"). |
| Two Python versions conflict | Always work inside the `navttc` environment: run `conda activate navttc` first. |

## Sample output

```text
$ conda --version
conda 24.1.2

$ python --version
Python 3.11.9

$ python -c "import torch; print(torch.__version__)"
2.3.0+cpu

$ python -c "import tensorflow as tf; print(tf.__version__)"
2.16.1

$ code --version
1.89.1
```
