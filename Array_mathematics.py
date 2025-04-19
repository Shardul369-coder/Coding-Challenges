"""
Task: 
You are given two integer arrays,A and B of dimensions N X M.Your task is to perform the following operations
1.Add(A+B)
2.Subtract(A-B)
3.Multiply(A*B)4
4.Integer Division (A/B)
5.Mod(A%B)
6.Power(A**B)

Note:
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.
"""

import numpy as np
n, m = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(n)])
B = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.floor_divide(A, B))  
print(np.mod(A, B))
print(np.power(A, B))
