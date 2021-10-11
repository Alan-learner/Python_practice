import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
ans = ''
for k in s:
    if k not in 'aeiouAEIOU':
        ans += k
print(ans)

"""
print(''.join([x for x in s if x not in 'aeuioAEUIO']))
"""