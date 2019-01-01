#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    l = []
    count = 0
    for i in range(n):
        if s[i]=='U':
            count += 1
        else:
            count -= 1
        l.append(count)
    valley_cnt =0
    #print(l)
    for i in range(n):
        if l[i] == -1 and l[i-1]==0:
            valley_cnt = valley_cnt+1
    return  valley_cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
