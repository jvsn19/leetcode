class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_idx = target_idx = 0
        len_start, len_target = len(start), len(target)

        while start_idx < len_start or target_idx < len_target:
            while start_idx < len_start and start[start_idx] == '_':
                start_idx += 1

            while target_idx < len_target and target[target_idx] == '_':
                target_idx += 1

            if start_idx == len_start or target_idx == len_target:
                return start_idx == len_start == target_idx == len_target

            if (start[start_idx] == target[target_idx] == 'L' and start_idx >= target_idx) \
                or (start[start_idx] == target[target_idx] == 'R' and start_idx <= target_idx):
                start_idx += 1
                target_idx += 1
            else:
                return False

        return start_idx == target_idx == len_start