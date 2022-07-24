class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def rob(nums):
            rob1 = 0
            rob2 = 0
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
    
        return max(nums[0], rob(nums[1:]), rob(nums[:-1]))