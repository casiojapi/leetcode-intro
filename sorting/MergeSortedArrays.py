class Solution:
    def merge(self, nums: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        
        nums1 = nums[:m]
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i +=1
            else:
                nums[k] = nums2[j]
                j +=1 
            k += 1
                
        while i < m:
            nums[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            nums[k] = nums2[j]
            j += 1
            k +=1 