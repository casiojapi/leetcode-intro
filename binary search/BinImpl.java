class Solution {
    public int search(int[] nums, int target) {
        int high = nums.length -1;
        int low = 0;
        
        while (low < high) {
            int mid = (low + high)/2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid -1;
            }
        }
        if (nums[low] == target)
            return low;
        return -1;
    }   
}