class Solution:
    def isPrefixOfWord(self, sentence: str, search_word: str) -> int:
        search_idx = 0
        word = 1
        
        for c in sentence:
            if c == " ":
                search_idx = 0
                word += 1

            elif search_idx != -1:
                if c == search_word[search_idx]:
                    search_idx += 1
                    
                    if search_idx == len(search_word):
                        return word
                else:
                    search_idx = -1

        return -1