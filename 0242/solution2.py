class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        char_count = {}
        
        # 统计s中字符出现频率
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            
        # 减去t中字符出现频率
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
                
        return len(char_count) == 0
"""
字典解法
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
"""