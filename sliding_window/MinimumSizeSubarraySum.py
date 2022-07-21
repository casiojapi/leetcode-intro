class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float("inf")
        currentSum = 0
        window = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            while currentSum >= target:
                minimum = min(minimum, abs(window - i) + 1)
                currentSum -= nums[window]
                window += 1
        if minimum > len(nums):
            minimum = 0
        return minimum