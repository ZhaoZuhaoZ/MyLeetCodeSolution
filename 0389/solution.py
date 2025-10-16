class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alphabet = [0] * 26

        for i in range(len(s)):
            n = ord(s[i]) - ord('a')
            alphabet[n] += 1

        for i in range(len(t)):
            n = ord(t[i]) - ord('a')
            alphabet[n] -= 1

        add = chr(ord('a') + alphabet.index(-1))

        return add