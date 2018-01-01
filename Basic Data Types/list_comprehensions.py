# Given three integers X, Y and Z representing the dimensions of a cuboid. You have to print a list of all possible coordinates
# on a 3D grid where the sum of i + j + k is not equal to N. 

# Input Format

# Four integers X,Y,ZX,Y,Z and N each on four separate lines, respectively.

# Output Format

# Print the list in lexicographic increasing order.

# Sample Input

# 1
# 1
# 1
# 2

# Sample Output

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print [ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range (z + 1) if ( ( i + j + k ) != n )]
