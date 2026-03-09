#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    unique_chars = list(set(s))
    max_length = 0
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            
            filtered = [char for char in s if char == char1 or char == char2]
            
            is_alternating = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]:
                    is_alternating = False
                    break
            
            if is_alternating:
                max_length = max(max_length, len(filtered))
                
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
