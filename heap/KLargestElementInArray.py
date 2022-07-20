class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        res = 0

        for i in range(k):
            res = heapq._heappop_max(nums)

        return res

    #vers 2

    def _findKthLargest(self, nums: List[int], k: int):
        k = len(nums) - k

        def quickSelect(left, right):
            pivot, p = nums[right], left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]

            if p > k: return quickSelect(left, p-1)
            elif p < k: return quickSelect(p + 1, right)
            else: return nums[p]
        
        return quickSelect(0, len(nums) - 1)