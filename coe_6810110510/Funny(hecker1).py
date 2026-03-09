#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    A = []
    for i in range(len(s)):
        if (i != len(s)-1):
           b = abs(ord(s[i])-ord(s[i+1]))
           A.append(b)
           b=0
    if A == A[::-1] :
        return "Funny"
    else:
        return "Not Funny"     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
