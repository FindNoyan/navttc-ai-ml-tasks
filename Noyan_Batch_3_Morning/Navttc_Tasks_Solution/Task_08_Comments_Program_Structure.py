# Task 08 — Comments and Program Structure
# Source: Week 1 syllabus, AI_NAVTTC_Outline_Tasks.pdf
# This example shows single-line comments, multi-line comments, a docstring,
# and a tiny well-structured program (area of a rectangle) with comments
# explaining each part.

# This is a SINGLE-LINE comment. It starts with # and Python ignores it.
# Use single-line comments to explain one line or one idea.

"""
This is a MULTI-LINE comment using triple double-quotes.
It can span several lines.
Python treats it as a long string that is not stored anywhere,
so it works as a block comment.
"""

'''
This is also a multi-line comment, using triple single-quotes.
Both styles are fine. Pick one and stay consistent.
'''


def rectangle_area(length, width):
    """This is a DOCSTRING: a comment inside a function.

    A docstring explains what the function does.
    It sits right after the 'def' line, inside triple quotes.
    """
    # Multiply length by width to get the area.
    area = length * width
    # Send the answer back to whoever called this function.
    return area


# --- Main program: the steps run in order, top to bottom ---

# Step 1: Set the inputs (the sides of the rectangle).
length = 8
width = 5

# Step 2: Call the function to do the calculation.
result = rectangle_area(length, width)

# Step 3: Show the result.
print("Length:", length)
print("Width:", width)
print("Area of rectangle:", result)

# Sample output:
# Length: 8
# Width: 5
# Area of rectangle: 40
