# 0389 找不同

## 思路
ASCII 求差：
    class Solution:
        def findTheDifference(self, s: str, t: str) -> str:
            return chr(sum(map(ord, t)) - sum(map(ord, s)))

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for ch in s + t:        # 拼接后一起异或
            xor ^= ord(ch)
        return chr(xor)

## 注意
chr map ord ^异或

## 复杂度
- 时间：O(n)
- 空间：O(1)

## 运行结果
- 执行用时：3 ms
- 内存消耗：17.76 MB