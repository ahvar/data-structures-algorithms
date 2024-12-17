"""
Find all subsequences of length k
Find all substrings of length j
"""
from rich import print as rprint
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)
k = 2
j = 4

chars = ['a','y','e','t','c','z','r','x','q']

# substrings
left = 0
substring = []
substrings = {}
for right in range(len(chars)):
    if (right + 1) - left < j:
        continue
    if right + 1 >= len(chars):
        substrings[chars[left]] = chars[left:right + 1]
        break
    if (right + 1) - left == j:
        substrings[chars[left]] = chars[left:right + 1]
        left += 1
        substring.clear()

pp.pprint(substrings)

# subsequences


