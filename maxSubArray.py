def maxSubArray(nums):
    if not nums:
        return 0

    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)

        if max_current > max_global:
            max_global = max_current

    return max_global

if __name__ == "__main__":

 print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
 print(maxSubArray([1]))
 print(maxSubArray([-1, -2, -3, -4]))
