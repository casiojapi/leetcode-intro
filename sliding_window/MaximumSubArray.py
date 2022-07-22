class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0 
        
        maxSum = nums[0]

        for i in range(len(nums)):
            if currentSum < nums[i] and currentSum < 0:
                currentSum = nums[i]
            else:
                currentSum += nums[i]
            maxSum = max(maxSum, currentSum)
            
        return maxSum