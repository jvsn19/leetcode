'''
More intuitive, but comes with extra O(N) in space
'''

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        queue_start, queue_target = [], []

        for idx in range(len(start)):
            if start[idx] != '_':
                queue_start.append((start[idx], idx))
            if target[idx] != '_':
                queue_target.append((target[idx], idx))

        while queue_start and queue_target:
            start_elem, start_idx = queue_start.pop()
            target_elem, target_idx = queue_target.pop()

            if start_elem != target_elem \
            or start_elem == 'L' and start_idx < target_idx \
            or start_elem == 'R' and start_idx > target_idx:
                return False

        return len(queue_start) == len(queue_target) == 0