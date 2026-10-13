# Task 42 — Pandas Getting Started
<!-- Source: https://www.w3schools.com/python/pandas_getting_started.asp -->
<!-- This guide shows how to install pandas, check that it works, and run a tiny first example. -->

## What is pandas?

Pandas is a Python library for working with tabular data (tables of rows
and columns). You will use it to load, inspect, clean, and analyze data
before doing any machine learning.

## Step 1 — Install pandas

Open a terminal (Command Prompt / PowerShell on Windows) and run:

```bash
pip install pandas
```

If you use Python 3 and `pip` points to Python 2, use:

```bash
pip3 install pandas
```

## Step 2 — Verify the installation

Run this command. If pandas is installed, it prints the version number
(such as `2.1.4`) instead of an error:

```bash
python -c "import pandas; print(pandas.__version__)"
```

## Step 3 — A tiny first example

Save the code below as `first_pandas.py` and run it with
`python3 first_pandas.py`. It imports pandas, makes a Series
(a single column of values), and prints it:

```python
import pandas as pd

# A Series is a one-dimensional labeled list of values.
marks = pd.Series([85, 92, 78, 88, 65])

print(marks)
```

## Sample output

Running the version check prints something like:

```text
2.1.4
```

Running the example prints:

```text
0    85
1    92
2    78
3    88
4    65
dtype: int64
```

The numbers `0` to `4` on the left are the default index labels.
`dtype: int64` means the values are whole numbers.
