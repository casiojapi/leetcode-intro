import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet hs = new HashSet();
        for (int i = 0; i < nums.length; i++) {
            if (!hs.contains(nums[i])) {
                hs.add(nums[i]);
            }
        }
        return hs.size() != nums.length;
    }
}