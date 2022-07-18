#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    count = 0 
    length = len(related)
    related = convertToArray(related)
    
    for index in range(length):
        if related[index][index] ==1:
            count +=1
            dfs(index, length, related)
    return count

def dfs(indx, length, matrix):
    if matrix[indx][indx] == 0:
        return
    for i in range(length):
        if matrix[indx][i] == 1:
            matrix[indx][i] = 0
            dfs(i, length, matrix)

def convertToArray(s):
    result = []
    for char in s:
        result.append([int(x) for x in char])
    return result
    
    