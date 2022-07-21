def findMaxSumSubarray(nums, k):
    res = float("-inf")
    currentMax = 0

    for i in range(nums):
        currentMax += nums[i]
     
        if i >= k -1:
            res = max(res, currentMax)
            currentMax -= nums[i - (k-1)]
    return res