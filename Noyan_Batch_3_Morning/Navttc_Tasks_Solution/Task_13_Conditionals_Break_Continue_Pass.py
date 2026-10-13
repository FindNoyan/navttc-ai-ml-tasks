# Task 13 — Conditionals, break, continue, pass
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows an if/elif/else grading example, plus a loop that
# demonstrates break (stop the loop), continue (skip one round), and
# pass (do nothing, placeholder).

# --- Part 1: if / elif / else grading example ---
# The conditions are checked top to bottom.
# The FIRST True condition runs, and the rest are skipped.
marks = 82
print("Marks:", marks)

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    # else runs only if NONE of the conditions above were True.
    grade = "F (Fail)"

print("Grade:", grade)

# --- Part 2: break, continue and pass in a loop ---

# break: STOP the loop completely, right away.
print("Break demo — stop when we reach 5:")
for number in range(1, 11):
    if number == 5:
        print("Found 5, breaking (stopping) the loop.")
        break  # exit the loop now; numbers 6-10 are never printed
    print(number)

# continue: SKIP the rest of this round and jump to the next number.
print("Continue demo — skip the number 3:")
for number in range(1, 6):
    if number == 3:
        print("Skipping 3.")
        continue  # skip the print below, go to the next number
    print(number)

# pass: DO NOTHING. It is a placeholder where Python needs a line of code
# but we do not want to do anything yet (useful while writing a program).
print("Pass demo — pass does nothing:")
for number in range(1, 4):
    if number == 2:
        pass  # placeholder: do nothing for number 2, keep looping
    print(number)
print("Loop finished. 'pass' did not stop or skip anything.")

# Sample output:
# Marks: 82
# Grade: A
# Break demo — stop when we reach 5:
# 1
# 2
# 3
# 4
# Found 5, breaking (stopping) the loop.
# Continue demo — skip the number 3:
# 1
# 2
# Skipping 3.
# 4
# 5
# Pass demo — pass does nothing:
# 1
# 2
# 3
# Loop finished. 'pass' did not stop or skip anything.
