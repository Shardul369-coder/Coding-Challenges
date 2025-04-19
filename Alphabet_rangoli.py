"""
You are given an integer,N.Your task is to print an alphabet rangoli of size N.(Rangoli is a form of Indian folk art based on creation of patterns.)
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

##Function Description
Complete the rangoli function in the editor below.
rangoli has the following parameters:
int size: the size of the rangoli

##Returns
string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
##Input Format
Only one line of input containing , the size of the rangoli.
###Constraints
0<size<27
"""

import string

def print_rangoli(size): 
    alpha = string.ascii_lowercase[:]
    lnm = []
    for i in range(size):
        left = '-'.join(alpha[size-1:i:-1])
        center = alpha[i]
        right = '-'.join(alpha[i+1:size])
        full = (left+'-'+center+'-'+right).strip('-')
        full.center(4*size-3,'-')
        lnm.append(full.center(4*size-3,'-'))
    print('\n'.join(lnm[::-1] + lnm[1:]))
  
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
