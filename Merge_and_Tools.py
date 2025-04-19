"""
Consider the following:

A string, s, of length n where s = C0c1...Cn-1
An integer, k, where k is a factor of n
We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once.
In other words, if the character at some index j in ti occurs at a previous index < j in ti, then do not include the character in string ui
Given s and k, print n/k lines where each line i denotes string ui


Input Format
The first line contains a single string denoting s.

The second line contains an integer, k, denoting the length of each subsegment.


Constraints
1 <= n <= 10**4, where n is the length of s
1 <= k <= n
It is guaranteed that n is a multiple of k

Output Format
Print n/k lines where each line i contains string ui

Explanation

String s is split into n/k = 9/3 = 3 equal parts of length k = 3. We convert each ti to ui by removing any subsequent occurrences non-distinct characters in ti:

t0 = AAB -> u0 -> AB
t1 = CAA -> u1 -> CA
t2 = ADA -> u2 -> AD
"""

def merge_the_tools(string, k):
   for i in range(0, len(string), k):
        chunk = string[i:i+k]
        ls = ''
        seen = set()
        for chunks in chunk:
            if chunks not in seen:
                seen.add(chunks)
                ls += chunks
        print(ls)    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

