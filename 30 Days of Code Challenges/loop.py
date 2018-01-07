# Given an integer, n, print its first 10 multiples.

import sys


n = int(raw_input().strip())

for i in range(1,11):
    print(str(n) + " x " + str(i) + " = " + str(n * (i)))
    
