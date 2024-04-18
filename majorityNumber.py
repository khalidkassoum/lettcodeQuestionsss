def majorityNumber(nums):
    number2 = None
    count = 0

    for num in nums:
        if count == 0:
            number2 = num
        count += (1 if num == number2 else -1)

    return number2


print(majorityNumber([2, 2, 1, 1, 1, 2, 2]))
