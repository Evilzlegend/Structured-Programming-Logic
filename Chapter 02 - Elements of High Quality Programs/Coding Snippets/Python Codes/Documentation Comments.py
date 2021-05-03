# TOPIC SUMMARY:
# Some comments are meant to explain the meaning of larger blocks of code. For example, we might
# want a paragraph of text to explain a multi-function program that is stored in a single file. Similarily,
# individual functions, classes, and methods may all need explanatory comments that go beyond a single
# phrase or sentence.

# TOPIC EXPLANATION:
# In Python these comments are called documentation strings or docstrings and they are written using
# Python's triple-quoted multiline strings.

# Good Python style requires docstring at the start of a file, to explain its purpose, and as the first item
# inside every class, function, or method definition.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

"""Contains functions for computing Euclidean distance in 2d and 3d."""
import math
def distance2d(pt1, pt2):
    """Takes in two coordinate points, each containing (x, y) values,
    and it returns the distance between them using Pythagorean theorem.
    """
    (x1, y1) = pt1
    (x2, y2) = pt2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def distance3d(pt1, pt2):
    """Takes in two coordinate points, each containing (x, y, z) values,
    and it returns the distance in 3d space extending Pythagorean theorem.
    """
    (x1, y1, z1) = pt1
    (x2, y2, z2) = pt2
    return math.sqrt((x1-x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

# Testing script here:
if __name__ == '__main__':
    twoPt1 = (35.6, 22)
    twoPt2 = (-120, 22.5)
    thrPt1 = (35.6, 22, 109)
    thrPt2 = (-119.99, 22.5, 105)
    d1 = distance2d(twoPt1, twoPt2)
    d2 = distance3d(thrPt1, thrPt2)
    print(d1, d2)