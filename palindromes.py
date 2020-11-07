def is_palindrome(num):

    nums = []

    while num > 0:
        nums.append(num % 10)
        n = n // 10

    if not nums:
        nums.append(0)

    for index in range(len(nums) // 2 + 1):
        if nums[index] != nu[-1 - index]:
            return False
        
    return True