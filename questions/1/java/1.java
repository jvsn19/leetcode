import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> prevNums = new HashMap<>();

        for (int idx = 0; idx < nums.length; ++idx) {
            int newTarget = target - nums[idx];

            if (prevNums.containsKey(newTarget)) {
                return new int[] {prevNums.get(newTarget), idx};
            }

            prevNums.put(nums[idx], idx);
        }

        return new int[] {-1, -1};
    }
}