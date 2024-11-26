public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var prevNums = new Dictionary<int, int>();

        for (var idx = 0; idx < nums.Length; ++idx) {
            var newTarget = target - nums[idx];

            if (prevNums.TryGetValue(newTarget, out int prevIdx)) {
                return new[] {prevIdx, idx};
            }

            prevNums[nums[idx]] = idx;
        }

        return new[] {-1, -1};
    }
}