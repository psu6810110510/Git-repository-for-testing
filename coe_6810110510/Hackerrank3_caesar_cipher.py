#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = []    
    k = k % 26
    O_lower = "abcdefghijklmnopqrstuvwxyz"
    O_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    A_lower = O_lower[k:] + O_lower[:k] 
    A_upper = O_upper[k:] + O_upper[:k]
    for char in s:
        if char in O_lower:
            index = O_lower.find(char)
            result.append(A_lower[index])
        elif char in O_upper:
            index = O_upper.find(char)
            result.append(A_upper[index])
        else:
            result.append(char)
            
    return "".join(result)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
