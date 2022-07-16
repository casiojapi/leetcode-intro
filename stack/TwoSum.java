import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap map = new HashMap<Integer, Integer>();
        int[] res = new int[2];
        //iterate the array (nums)
        for (int i = 0; i < nums.length; i++ ) {
            int value = target - nums[i];
            if (map.containsKey(value)) {
                res[0] = (int)map.get(value);
                res[1] = i;
                return res;
            }
                
            map.put(nums[i], i);
        }
        res[0] = -1;
        res[1] = -1;
        return res;
    }
}