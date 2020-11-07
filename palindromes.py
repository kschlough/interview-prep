def is_palindrome(num):

    nums = []

    while num > 0:
        nums.append(num % 10)
        # // throws away the remainder when dividing
        n = n // 10

    if not nums:
        nums.append(0)

    # option 1:
    return nums == list(reversed(nums))

    # option 2:
    for index in range(len(nums) // 2 + 1):
        if nums[index] != nu[-1 - index]:
            return False
        
    return True


# could also try:
# follow lines 5-8 to put in list, then use python reverse function on list