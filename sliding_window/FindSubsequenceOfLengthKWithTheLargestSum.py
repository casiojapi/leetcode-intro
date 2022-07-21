class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        indexSet = set()
        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i], i))
            indexSet.add(i)
            if (len(minHeap) > k):
                x, index = heapq.heappop(minHeap)
                indexSet.remove(index)
                
        res = []
        for i in range(len(nums)):
            if i in indexSet:
                res.append(nums[i])
        return res