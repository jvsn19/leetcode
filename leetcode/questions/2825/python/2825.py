class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        len_str_1, len_str_2 = len(str1), len(str2)

        if len_str_2 > len_str_1:
            return False

        idx_2 = 0

        for idx_1, chr_1 in enumerate(str1):
            int_chr_1 = ord(chr_1)

            # compare the current caracter with the str_2[idx_2], it's next (+ 1) and it's next in loop 
            # (-25, z(122) - a(97))
            if idx_2 < len_str_2 and (ord(str2[idx_2]) in [int_chr_1, int_chr_1 + 1, int_chr_1 - 25]):
                idx_2 += 1

        return idx_2 == len(str2)