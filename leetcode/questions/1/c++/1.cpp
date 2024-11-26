#include <vector>
#include <map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int> nums, int target) {
        std::map<int, int> prevNums;

        for (int idx = 0; idx < nums.size(); ++idx) {
            int newTarget = target - nums[idx];

            if (prevNums.find(newTarget) != prevNums.end()) {
                return {prevNums[newTarget], idx};
            }

            prevNums[nums[idx]] = idx;
        }

        return {-1, -1};
    }
};