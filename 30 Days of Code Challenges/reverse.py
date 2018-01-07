# Given an array, A, of N integers, print A's elements in reverse order as a 
# single line of space-separated numbers. 
# sample input
# 4
# 1 4 3 2
# sample output: 2 3 4 1

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
for item in reversed(arr):
    print item,
