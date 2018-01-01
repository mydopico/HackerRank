# Task
# Initialize your list (L = []) and follow the NN commands given over NN lines.

# Each command will be 11 of the 88 commands given above. The extend(LL) method will not be used. Each command will have its own value(s) separated by a space.

# Input Format

# The first line contains an integer, NN (the number of commands).
# The NN subsequent lines each contain one of the 88 commands described above.

# Sample Input

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

N = int(raw_input())
    
list = []
    
for i in range(N): 
        option = raw_input().split()
        if option[0] == 'print':
            print(list)
        elif option[0] == 'sort':
            list.sort()
        elif option[0] == 'remove':
            list.remove(int(option[1]))
        elif option[0] == 'append':
            list.append(int(option[1]))
        elif option[0] == 'insert':
            list.insert(int(option[1]),int(option[2]))
        elif option[0] == 'reverse':
            list.reverse()
        elif option[0] == 'pop':
            list.pop()
