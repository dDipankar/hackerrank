#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=0
    count =0
    while i<len(c)-1:
        if c[i]==1:
            i= i+1
        elif c[i]==0:
            if i+2<=len(c)-1 and c[i+2]==0:
                i=i+2
            elif c[i+1]==0:
                i=i+1
            count = count +1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
