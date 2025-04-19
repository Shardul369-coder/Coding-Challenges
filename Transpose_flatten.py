"""
Task:
You are given a N X M integer array matrix with space separated elements (N= rows and M= columns).
Your task is to print the transpose and flatten results.

##Input Format
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.
##Output Format
First,print the transpose array and then print the flatten.
"""

import numpy as np
rows, cols = map(int, input().split())
total = []
for _ in range(rows):  
    num = list(map(int,input().split()))  
    total += num  

g = np.array(total)
k = g.reshape(rows,cols)
print(k.T)
print(k.flatten())
