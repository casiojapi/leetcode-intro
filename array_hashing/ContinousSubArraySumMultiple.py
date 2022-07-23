class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #porque 0 -1
        prefixes = {0 : -1}
        prefix = 0
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % k
            if prefix not in prefixes:
                prefixes[prefix] = i
            elif i - prefixes[prefix] > 1:
                return True
        return False  