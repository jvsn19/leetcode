from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        chars = []
        spaces_idx = 0

        for idx, c in enumerate(s):
            if spaces_idx < len(spaces) and idx == spaces[spaces_idx]:
                chars.append(" ")
                spaces_idx += 1
            
            chars.append(c)

        return "".join(chars)