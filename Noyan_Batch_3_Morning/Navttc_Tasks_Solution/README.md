# NAVTTC Tasks — Solutions (Weeks 1–5)

Solutions for Tasks 1–52 from Annexure-I of the NAVTTC AI/ML course outline
(`AI_NAVTTC_Outline_Tasks.pdf`). For every topic that has a tutorial link
(w3schools / GeeksforGeeks / Programiz / etc.), one representative example is
solved with comments explaining the logic.

Every `.py` file is self-contained and runnable with `python3 <file>`.
NumPy files need `numpy`, Pandas files need `pandas`, Week 5 files need
`scikit-learn`: `pip install numpy pandas scikit-learn`

## Week 1 — Python Fundamentals

| Task | File | Topic |
|---|---|---|
| 1 | Task_01_Installation.md | Installation: Anaconda, PyTorch, TensorFlow, VS Code, PyCharm |
| 2 | Task_02_Linux_Commands.sh | Linux commands (demo script; dangerous commands commented only) |
| 3 | Task_03_Values_Expressions_Statements.py | Values, expressions, statements |
| 4 | Task_04_Numbers_Booleans_Strings.py | Numbers, Booleans, Strings |
| 5 | Task_05_Operators_Variables_Keywords.py | Operators, variables, keywords |
| 6 | Task_06_String_Operations.py | String operations |
| 7 | Task_07_Input_Type_Casting.py | Input and type casting |
| 8 | Task_08_Comments_Program_Structure.py | Comments and program structure |
| 9 | Task_09_Lists_Basics.py | Lists basics |
| 10 | Task_10_Tuples_Basics.py | Tuples basics |
| 11 | Task_11_Dictionaries_Basics.py | Dictionaries basics |
| 12 | Task_12_Sets_Basics.py | Sets basics |
| 13 | Task_13_Conditionals_Break_Continue_Pass.py | if/elif/else, break, continue, pass |
| 14 | Task_14_Nested_Conditionals_Ternary.py | Nested conditionals, ternary expression |
| 15 | Task_15_For_Loops.py | for loops |
| 16 | Task_16_While_Loops.py | while loops |
| 17 | Task_17_Break_Statement.py | break statement |
| 18 | Task_18_Continue_Statement.py | continue statement |
| 19 | Task_19_Looping_Techniques.py | Looping techniques (enumerate, zip, reversed, sorted) |
| 21 | Task_21_List_Methods.py | List methods |
| 22 | Task_22_Tuple_Operations.py | Tuple operations |
| 23 | Task_23_String_Methods.py | String methods |
| 24 | Task_24_Set_Operations.py | Set operations |
| 25 | Task_25_Dictionary_Methods.py | Dictionary methods |

## Week 2 — Functions, Exceptions, Statistics

| Task | File | Topic |
|---|---|---|
| 20 | Task_20_User_Defined_Functions.py | User-defined functions (scope, lambda, map/filter) |
| 26 | Task_26_Exception_Handling.py | Exception handling (try/except/finally) |
| 27 | Task_27_User_Defined_Exceptions.py | User-defined exceptions |
| 49 | Task_49_Mean_Median_Mode.py | Mean, median, mode |
| 50 | Task_50_Standard_Deviation.py | Standard deviation |

## Weeks 3–4 — NumPy and Pandas

| Task | File | Topic |
|---|---|---|
| 28 | Task_28_Numpy_Creating_Arrays.py | Creating NumPy arrays |
| 29 | Task_29_Numpy_Indexing.py | NumPy indexing |
| 30 | Task_30_Numpy_Slicing.py | NumPy slicing |
| 31 | Task_31_Numpy_Data_Types.py | NumPy data types |
| 32 | Task_32_Numpy_Copy_vs_View.py | Copy vs view |
| 33 | Task_33_Numpy_Array_Shape.py | Array shape |
| 34 | Task_34_Numpy_Array_Reshape.py | Array reshape |
| 35 | Task_35_Numpy_Array_Iterating.py | Array iterating |
| 36 | Task_36_Numpy_Array_Joining.py | Array joining |
| 37 | Task_37_Numpy_Array_Splitting.py | Array splitting |
| 38 | Task_38_Numpy_Array_Searching.py | Array searching |
| 39 | Task_39_Numpy_Array_Sorting.py | Array sorting |
| 40 | Task_40_Numpy_Random.py | NumPy random |
| 41 | Task_41_Pandas_Basics.py | Pandas basics |
| 42 | Task_42_Pandas_Getting_Started.md | Pandas installation / getting started |
| 43 | Task_43_Pandas_Series.py | Pandas Series |
| 44 | Task_44_Pandas_DataFrame.py | Pandas DataFrame |
| 45 | Task_45_Pandas_Reading_CSV.py | Reading CSV files |
| 46 | Task_46_Pandas_Analyzing_Data.py | Analyzing data |
| 47 | Task_47_Pandas_Data_Cleaning.py | Data cleaning |
| 48 | Task_48_Pandas_Correlations.py | Data correlations |

## Week 5 — Machine Learning I

| Task | File | Topic |
|---|---|---|
| 51 | Task_51_Linear_Regression.py | Linear regression with scikit-learn |
| 52 | Task_52_Logistic_Regression.py | Logistic regression with scikit-learn |

## Notes

- Tasks 3–14 are blank ("Python") in the PDF; they are mapped to the Week 1
  syllabus fundamentals (see table above).
- Tasks 9–12 cover the basics of each data type; Tasks 21–25 cover the
  methods/operations for the same types with different examples.
- Task 2's shell script is a demo: dangerous commands (shutdown, restart, rm,
  kill, sudo) appear only as comments. Check it with `bash -n`, don't run it
  blindly.
- Tasks 51–52 were compiled but not executed here because scikit-learn was not
  installed in this environment. Run them once where scikit-learn is installed
  to confirm the printed results.
