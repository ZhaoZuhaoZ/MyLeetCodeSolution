class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        common_len = min(len(word1),len(word2))
        output = ""

        for i in range(0, common_len, 1):
            output = output + word1[i] 
            output = output + word2[i] 
        
        if len(word1) != common_len:
            output = output + word1[common_len:] 
        elif len(word2) != common_len:
            output = output + word2[common_len:] 
        
        return output