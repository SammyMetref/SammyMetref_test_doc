"""My dumb math tools
This is a collection of math tools i often use. 
This is also an example code to test the automatic building of a code documentation.
"""

import numpy as np
import random as rd


print(f"Name: {__name__}")
print(f"Package: {__package__}")

print("This is a collection of math tools i often use.")

def __init__():
    param=3.14

def main():
    """Example application: compute ((a+b)*2) where a=3, b=5."""
    msg = "Example application: compute ((a+b)*2) where a=3, b=5:"
    print(msg)
    print('RESULT:')
    res_add = add(3,5)
    res_mul = mul(res_add,2)
    print(res_mul)


def add(a, b):
    """Add two numbers and return the result.

    Parameters
    ----------
    arg1 : float
        First number to sum.
    arg2 : float
        Second number to sum.

    Returns
    -------
    float
        Addition of the two numbers.

    """
    return a + b
