#hackerrank interview prep kit

# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

# Example


# -9 -9 -9  1 1 1 
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
# The  hourglass sums are:

# -63, -34, -9, 12, 
# -10,   0, 28, 23, 
# -27, -11, -2, 10, 
#   9,  17, 25, 18
# The highest hourglass sum is  from the hourglass beginning at row , column :

# 0 4 3
#   1
# 8 6 6
# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

# Function Description

# Complete the function hourglassSum in the editor below.

# hourglassSum has the following parameter(s):

# int arr[6][6]: an array of integers
# Returns

# int: the maximum hourglass sum
# Input Format

# Each of the  lines of inputs  contains  space-separated integers .

# Constraints

# Output Format

# Print the largest (maximum) hourglass sum found in .

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19
# Explanation

#  contains the following hourglasses:

# image
# The hourglass with the maximum sum () is:

# 2 4 4
#   2
# 1 2 4

def hourglassSum(arr):
    print(arr)
    hourglass_sums = []
    
    for i in range(1, (len(arr)- 1)):
        print(arr[i])
        for j in range(1, len(arr[i])- 1):
            print(arr[i][j])
            hourglass = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j] + arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            hourglass_sums.append(hourglass)
            
    return max(hourglass_sums)
    
    
    
# pseudocode
    # starting point is always the middle 4x4
    # iterate through arr[0 + 1] through arr[len - 1]
        # then iterate through each array's [0 + 1] to [len - 1]
        # calc the value of positions: 
            #[row - 1][i-1][row - 1][i][row-1][i+1] 
            #[row +1][i-1][row + 1][i][row+1][i+1]
        # never have to worry about it being out of bounds
        # add the value of each position as a sum to array
        # return the highest num from the array
