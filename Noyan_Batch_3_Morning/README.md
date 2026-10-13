# Noyan — Batch 3 Morning

NAVTTC AI/ML coursework (Netsol), Weeks 1–5.

## Folder structure

```
Noyan_Batch_3_Morning/
├── README.md                    ← this file
├── Navttc_Tasks_Solution/       ← NAVTTC outline tasks 1–52 (Weeks 1–5)
│   ├── README.md                ← index of all tasks by week
│   └── Task_XX_<Topic>.py       ← one file per task
└── Class_Tasks_Solution/        ← class tasks (placeholder for now)
    └── README.md
```

- **Navttc_Tasks_Solution/** — solutions for the tasks in Annexure-I of
  `AI_NAVTTC_Outline_Tasks.pdf`. Where a topic has a tutorial link
  (w3schools / GeeksforGeeks / Programiz / etc.), one representative example
  is solved for that topic, with comments explaining the logic.
- **Class_Tasks_Solution/** — reserved for the class tasks the teacher gives
  in class. They are not shared yet, so this folder holds only a placeholder
  README. Solutions will be added here when the tasks arrive.

## How to run

```bash
# Weeks 1–2 (pure Python, no extra packages needed)
python3 Navttc_Tasks_Solution/Task_15_For_Loops.py

# Weeks 3–5 (needs libraries)
pip install numpy pandas scikit-learn
python3 Navttc_Tasks_Solution/Task_28_Numpy_Creating_Arrays.py
python3 Navttc_Tasks_Solution/Task_51_Linear_Regression.py
```

Notes:
- Task 1 is a Markdown install guide (`Task_01_Installation.md`).
- Task 2 is a shell demo script (`Task_02_Linux_Commands.sh`) — check it with
  `bash -n Task_02_Linux_Commands.sh`; dangerous commands are comments only.
- Every `.py` file is self-contained: no downloads, no external data files.
- Tasks 51–52 (scikit-learn) were compiled but not executed in this
  environment because scikit-learn was not installed. Run them once where it
  is installed to confirm the printed results.

## Source

Course outline: `AI_NAVTTC_Outline_Tasks.pdf` (Annexure-I, Tasks 1–52).
GitHub repo (not pushed to yet): https://github.com/FindNoyan/navttc-ai-ml-tasks
