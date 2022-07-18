class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        appearances = {}
        for i in range(0, len(nums)):
            if nums[i] in appearances:
                continue
            appearances.update({nums[i], i})
            if (target - nums[i]) in appearances:
                return (i, appearances.get(target - nums[i]))
        
            
        