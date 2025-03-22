"""
Q.Two players, Kevin and Stuart, are playing a word game using a given string. The game follows these rules:
1.The players take turns forming substrings using the given string.
2.Kevin scores points for substrings that start with a vowel (A, E, I, O, U).
3.Stuart scores points for substrings that start with a consonant (all other letters).
4.The score for a substring is determined by the number of times it appears as a starting sequence in the string.
"""
def minion_game(string):
    # your code goes here
    n = len(string)
    comb = ((n)*(n+1))/2
    count_k = 0
    count_s = 0
    count_k = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    count_s = comb - count_k
    
    if count_s == count_k:
        print("Draw")
    elif count_s > count_k:
        print("Stuart", int(count_s) )
    else:
        print("Kevin", int(count_k))

if __name__ == '__main__':
    s = input()
    minion_game(s)
