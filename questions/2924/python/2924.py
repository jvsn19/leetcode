from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        strongests = {node for node in range(n)}

        for _, v in edges:
            strongests.discard(v)

        return strongests.pop() if len(strongests) == 1 else - 1