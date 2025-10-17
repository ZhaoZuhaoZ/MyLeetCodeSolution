class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            map = [0] * 26

            for i in range(len(s)):
              x = ord(s[i]) - ord('a')
              y = ord(t[i]) - ord('a')
              map[x] += 1
              map[y] -= 1

            if map == [0] * 26:
              return True
        
        return False

"""
哈希表，只用于存储字母出现的频率
时间复杂度：O(n)
空间复杂度：O(1)
"""