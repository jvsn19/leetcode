from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}

        for idx, num in enumerate(nums):
            new_target = target - num

            if new_target in prev_nums:
                return prev_nums[new_target], idx

            prev_nums[num] = idx

        return [-1, -1]