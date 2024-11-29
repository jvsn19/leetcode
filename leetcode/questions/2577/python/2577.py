import heapq

from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        
        n_rows, n_cols = len(grid), len(grid[0])
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def find_minimum_time():
            next_positions = [(0, 0, 0)]
            visited = set()

            while next_positions:
                time, row, col = heapq.heappop(next_positions)

                if row == (n_rows - 1) and col == (n_cols - 1):
                    return time

                if (row, col) in visited:
                    continue

                visited.add((row, col))

                for row_inc, col_inc in steps:
                    new_row, new_col = row + row_inc, col + col_inc

                    if (0 <= new_row < n_rows) and (0 <= new_col < n_cols) and (new_row, new_col) not in visited:
                        # If the time difference between current and next time is greater than one we need to keep
                        # going back and forward until we hit that time. In other words we will increase the current
                        # time by 2 while the current time is smaller than the next time.

                        # If the time difference is even, it means that we'll surpass the next time by one (remember, 
                        # we always move the time 2 by 2)
                        # Example: diff time is 8 (2 and 10) the current times will be 2, 4, 6, 8, 10 and then from 10
                        # to 11 because it takes one more second to walk.
                        extra_time = 1 if (grid[new_row][new_col] - time) & 1 == 0 else 0

                        # The next time is the maximum between the current time + 1, meaning that the next time is already
                        # smaller than the current; and the next_time + extra_time, in case we need to wait
                        heapq.heappush(
                            next_positions, 
                            (max(time + 1, grid[new_row][new_col] + extra_time), new_row, new_col))

            return -1

        return find_minimum_time()