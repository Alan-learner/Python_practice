import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
cnt = len(set(s.lower().replace(' ','')))
if cnt == 26:
    res = 'true'
else:
    res = 'false'

print(res)


"""
import string
print("true") if len(set(filter(lambda x: x.isalpha(), input().lower()))) == len(string.ascii_lowercase) else print("false")
"""