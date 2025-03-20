"""
Task:
You will receive space-separated integers as input, each representing the size of a dimension in an array. Your task is to create and print:
1) A NumPy array of zeros with the given shape.
2) A NumPy array of ones with the same shape.

Hint:
Use numpy.zeros() and numpy.ones() to achieve this.
"""


#First Approach
import numpy as np
value = list(map(int, input("Enter Dimensions: ").split()))  
if len(value) == 3:
    a,b,c = value
    t = []
    for i in range(a):
        t.append(np.zeros((b,c),dtype=int))
    m = np.stack(t,axis=0)
    print(m)
    z = []
    for i in range(a): 
        z.append(np.ones((b,c),dtype=int))
    n = np.stack(z,axis=0)
    print(n)

elif len(value) == 2:
    a,b = value
    t = []
    for i in range(a):
        t.append(np.zeros((b),dtype=int))
    m = np.stack(t,axis=0)
    print(m)
    z = []
    for i in range(a): 
        z.append(np.ones((b),dtype=int))
    n = np.stack(z,axis=0)
    print(n)

elif len(value) == 4:
    a,b,c,d = value
    t = []
    for i in range(a):
        t.append(np.zeros((b,c,d),dtype=int))
    m = np.stack(t,axis=0)
    print(m)
    z = []
    for i in range(a): 
        z.append(np.ones((b,c,d),dtype=int))
    n = np.stack(z,axis=0)
    print(n)


#Optimized Code
import numpy as np

value = list(map(int, input("Enter Dimensions: ").split()))

if len(value) == 3:
    a, b, c = value
    m = np.zeros((a, b, c), dtype=int)
    n = np.ones((a, b, c), dtype=int)

elif len(value) == 2:
    a, b = value
    m = np.zeros((a, b), dtype=int)
    n = np.ones((a, b), dtype=int)

elif len(value) == 4:
    a, b, c, d = value
    m = np.zeros((a, b, c, d), dtype=int)
    n = np.ones((a, b, c, d), dtype=int)

print(m)
print(n)


#Expected Output
"""
Enter Dimensions: 3 3 3
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
"""
#OR
"""
Enter Dimensions: 3 2
[[0 0]
 [0 0]
 [0 0]]
[[1 1]
 [1 1]
 [1 1]]
"""
#OR
"""
Enter Dimensions: 3 2 2 2
[[[[0 0]
   [0 0]]

  [[0 0]
   [0 0]]]


 [[[0 0]
   [0 0]]

  [[0 0]
   [0 0]]]


 [[[0 0]
   [0 0]]

  [[0 0]
   [0 0]]]]
[[[[1 1]
   [1 1]]

  [[1 1]
   [1 1]]]


 [[[1 1]
   [1 1]]

  [[1 1]
   [1 1]]]


 [[[1 1]
   [1 1]]

  [[1 1]
   [1 1]]]]
"""
