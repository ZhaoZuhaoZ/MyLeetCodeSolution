class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for slow in range(len(haystack)):
            if ord(haystack[slow]) ^ ord(needle[0]) == 0:
                i = 1
                while (i < min(len(needle),len(haystack)-slow)) and (ord(haystack[i+slow]) ^ ord(needle[i]) == 0):
                    i += 1 
                if i == len(needle):
                    return slow
        return -1