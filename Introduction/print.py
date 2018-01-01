# Read an integer N.

# Without using any string methods, try to print the following:

# 123...N

# Input Format
# The first line contains an integer N.

# Output Format
# Output the answer as explained in the task.

# Sample Input

# 3

# Sample Output

# 123

from __future__ import print_function # print without spaces 

def print_values(n):   

   for i in range (0, n):
       print (i+1,end='') # print without spaces and discard newlines
   
   
    
    
n = int(raw_input())
print_values(n)


