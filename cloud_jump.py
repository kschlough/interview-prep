
# Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

# For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes .

# Function Description

# Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

# jumpingOnClouds has the following parameter(s):

# c: an array of binary integers
# Input Format

# The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .

# Constraints

# Output Format

# Print the minimum number of jumps needed to win the game.

# Sample Input 0

# 7
# 0 0 1 0 0 1 0
# Sample Output 0

# 4
# Explanation 0:
# Emma must avoid c[2] and c[5]. She can win the game with a minimum of 4 jumps


# this should always find the min without having to compare data for 2 routes
import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    # first check if c[0] is a 1, because then no jumps
    if c[0] == 1:
        return 0
    
    jump_count = 0
    
    # starting at c[1] because you start on c[0] and don't jump to get there 
    current_index = 0   
    while current_index < len(c):
        print(c[current_index])
        current_index += 1
        # # if there are 2 more numbers available
        # if c[(current_index+2)]:
        #     # if 2 more numbers is 0
        #     if c[current_index+2] == 0:
        #         current_index += 2
        #         jump_count += 1
        #     # if 2 more numbers is 1
        #     elif c[current_index+1] == 0:
        #         current_index += 1
        #         jump_count += 1
        # # if there's only 1 more number available
        # if c[(current_index+1)]:
        #     if c[current_index+1] == 0:
        #         current_index += 1
        #         jump_count += 1
        #     elif c[current_index + 1] != 0:
        #         return jump_count
        
        # return jump_count

print(jumpingOnClouds([0,0,1,0,0,1,0]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
