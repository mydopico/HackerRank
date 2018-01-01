# Task
# You are given the year, and you have to write a function to check if the year is leap or not.

# Input Format

# Read y, the year that needs to be checked.

# Output Format

# Output is taken care of by the template. Your function must return a boolean value (True/False)

# Sample Input

# 1990  

# Sample Output

# False  

# Explanation

# 1990 is not a multiple of 4 hence it's not a leap year. 

def is_leap(year):      
    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:    
       return True
    else:
       return False
