# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains n. The second line contains an array of integers n each separated by a space. 

# Output Format

# Output the value of the second largest number.

# Sample Input

# 5
# 2 3 6 6 5
# Sample Output

# 5

n = int(raw_input())
arr = map(int, raw_input().split())
    
my_score = set(arr)
my_score.remove(max(my_score))
print max(my_score)
