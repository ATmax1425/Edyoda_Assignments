from itertools import combinations


def is_Palindrome(s: str):
    return s == s[::-1]


string = input()
comb = combinations(range(len(string) + 1), 2)
count = 0
for i, j in comb:
    if is_Palindrome(string[i:j]):
        count += 1
print(count)
