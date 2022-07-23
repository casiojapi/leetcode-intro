class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        #prefixes sums, key = sum and value = amount of subarrays that has that value
        # i initialize 0: 1, as a sub array plus 0,
        prefixes = {0: 1}
        #i iterate over all main array indexes
        for i in range(len(nums)):
            #calculate the current till this value
            currSum += nums[i]
            # calculate de diff (how much do we need to get to K)
            diff = currSum -k
            #and search for the amount of subarrays that can get me that diff
            # if i dont have that diff in the prefixes, i return 0, so the res will not be updated
            res += prefixes.get(diff, 0)
            #and then I add the current sum value to the prefixes map for the next iterations
            prefixes[currSum] = 1 + prefixes.get(currSum, 0)
        return res