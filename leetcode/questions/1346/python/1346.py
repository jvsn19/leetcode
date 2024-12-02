from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        prevs = set()

        for num in arr:
            if num * 2 in prevs or num / 2 in prevs:
                return True

            prevs.add(num)
        
        return False