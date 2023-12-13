"""
Name: Jackson McAfee
Date: 11-27-2023
Assignment: Module 13: Python Dask Multi Task
Due Date: 11-26-2023
About this project: I am using the first alternative harmonic series listed online.
                    That is the series: 1 - 1/2 + 1/3 - 1/4 ... = ln(2)

                    This script approximates the series above using DASK before 
                    displaying the approximation.

Assumptions: N/A
All work below was performed by Jackson McAfee
"""

import dask.delayed as delayed
from dask.diagnostics import ProgressBar
from math import log

# if it is an even denominator, it is negative
def neg(x):
    return (-1/x)

# if it is an odd denominator, it is positive
def pos(x):
    return (1/x)

# sum the two values passed in
def final_sum(x, y):
    return (x + y)

def main():
    # define list upper bound
    maxSize = 10000

    # create lists of values to pass in 
    oddVals = [*range(1, maxSize, 2)]
    evenVals = [*range(2, maxSize, 2)] 

    # do something
    posOdd = [delayed(pos)(i) for i in oddVals]
    negEven = [delayed(neg)(j) for j in evenVals]
    sumOdd = delayed(sum)(posOdd)
    sumEven = delayed(sum)(negEven)
    result = delayed(final_sum)(sumOdd, sumEven)

    # print results
    with ProgressBar():
        print("Computed result: ", result.compute())
        print("Expected result: ", log(2))

if __name__ == "__main__":
    main()
   
