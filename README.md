# Python Function Bug: TypeError in calculate_average()

This repository demonstrates a common error in Python functions: the improper handling of input types that leads to a `TypeError`. The `calculate_average()` function fails when the input list contains non-numeric values.

The `bug.py` file contains the buggy code, while `bugSolution.py` presents the solution.

## Bug Description
The function `calculate_average()` calculates the average of numbers in a list.  However, it lacks error handling for non-numeric data types.  If a string or other non-numeric type is in the list, a `TypeError` will occur during the `sum()` operation.

## Solution
The solution implements input validation to check that all elements in the input list are numbers.  If a non-numeric element is detected, an appropriate message is printed, or an exception is raised, preventing the program from crashing.