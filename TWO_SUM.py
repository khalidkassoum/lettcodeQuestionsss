def two_sum(nums, target):
    num_dic = {}
    for index, num in enumerate(nums):
        mynumm = target - num
        if mynumm in num_dic:
            return [num_dic[mynumm], index]
        num_dic[num] = index
    return []


nums = [3, 8, 14, 17]
target = 11
print(two_sum(nums, target))
