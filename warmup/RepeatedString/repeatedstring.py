#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    lens = len(s)
    repeat = int(n/lens)
    reminder = n % lens
    count_a =0
    for i in range(lens):
        if s[i]=='a':
            count_a +=1
    count_a += (repeat -1)*count_a
    for i in range(reminder):
        if s[i] == 'a':
            count_a += 1
    return count_a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
