# Task
# You are given an integer, n, on a single line. The next line contains n space-separated integers. Create a tuple, t, of those n
# integers, then compute and print the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module.

# Input Format

# The first line contains an integer, n (the number of elements in the tuple).
# The second line contains n space-separated integers describing t.

# Output Format

# Print the result of hash(t).

# Sample Input

# 2
# 1 2
# Sample Output

# 3713081631934410656

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    
    print hash(integer_list)

