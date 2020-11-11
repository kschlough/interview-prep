# Write a function to find the rectangular intersection of two given rectangles.

# Rectangles are always "straight" and never "diagonal" (their edges will always be perpendicular to the axes).

# A rectangle will be represented as follows

# rectangle = {
#    # Coordinates of bottom-left corner
#    'left_x'   : 1,
#    'bottom_y' : 1,

#    # Width and height
#    'width'    : 6,
#    'height'   : 3,
# }

# Your output/result rectangle should be of this format also.

# questions:
# negative coordinates: shouldn’t matter, solution should work for negative coordinates (height & width coordinates will always be positives)
# can you have two rectangles that don’t overlap at all? yes


# pseudocode:
# do they cross on the x-axis
    # what's the minimum point of intersection
# do they cross on the y-axis
    # what's the min point of intersection
# if yes to both: overlap
    # else if no to one or both: no overlap

# code:

def is_overlapping(rect_1, rect_2):
    # starting x
    if rect_1['left_x'] > rect_2['left_x']:
        start_x = rect_1['left_x']
    else:
        start_x = rect_2['left_x']
    print(start_x) #5

    # find min point of intersection x
    x_min = min((rect_1['left_x'] + rect_1['width']), 
        (rect_2['left_x'] + rect_2['width']) 
        ) #7
    
    # starting y
    if rect_1['bottom_y'] > rect_2['bottom_y']:
        start_y = rect_1['bottom_y']
    else:
        start_y = rect_2['bottom_y']
    print(start_y) #2
    
    # find min point of intersection y
    y_min = ((rect_1['bottom_y'] + rect_1['height']),
        (rect_2['bottom_y'] + rect_2['height'])
        ) #4
    
    # if min point of intersection is greater than larger start x, they overlap
    
    if x_min > start_x and (y_min > start_y):
        print("Yes, there is overlap")
        overlap_rect = {
            'left_x': x_min,
            'bottom_y': y_min,
            # 'width':
            # 'height':
        }
        return overlap_rect       

    
# test cases:

# usual overlap:
rect_1 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 6,
    'height': 3
}

rect_2 = {
    'left_x': 5,
    'bottom_y': 2,
    'width': 3,
    'height': 3
}
is_overlapping(rect_1, rect_2)
# prints "Yes, there is overlap"
# returns
    # {
    #     'left_x': 5,
    #     'bottom_y': 2,
    #     'width': 2,
    #     'height': 2
    # }

# touches but no overlap
rect_3 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 6,
    'height': 3
}

rect_4 = {
    'left_x': 7,
    'bottom_y': 4,
    'width': 3,
    'height': 3
}
is_overlapping(rect_3, rect_4)
# prints "No, there is no overlap"
# no return

# no overlap
rect_5 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 6,
    'height': 3
}

rect_6 = {
    'left_x': 9,
    'bottom_y': 5,
    'width': 3,
    'height': 3
}
is_overlapping(rect_5, rect_6)
# prints "No, there is no overlap"
# no return