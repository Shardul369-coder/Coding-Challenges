"""
Task:
You are given a polynomial P of a single indeterminate (or variable),x.
You are also given the values of x and k. Your task is to verify if P(x) = k.

##Constraints
All coefficients of polynomial P are integers.
x and y are also integers.

##Input Format
The first line contains the space separated values of x and k.
The second line contains the polynomial P.
##Output Format
Print True if P(x) = k.Otherwise, print False.

##Explanation
p(1) = 1**3+1**2+1 = 4 = k
Hence, the output is True.
"""

x,k = map(int,input().split())
p = input()
result = eval(p)
if result == k:
    print(True)
else:
    print(False)
