# 0028 找出字符串中第一个匹配项的下标

## 思路

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def build_next(pattern):
            n = len(pattern)
            j = 0
            next = [0] * n

            for i in range(1,n,1):
                
                """
                如果不匹配，前缀j不要直接回到开头
                要让前面匹配过的前缀用起来
                现在是
                已匹配的前缀1   -B-XXXXXXXX-   已匹配的后缀1-A
                已匹配的前缀2-XX-B-XXXXXXXX-XX-已匹配的后缀2-A
                现在存在一个问题，前缀2一定匹配的是后缀1退出来的东西，后缀2一定匹配的是前缀1退出来的东西
                若想要前缀2与后缀2匹配，那么前缀1（后缀1）本身就得前后匹配
                在已匹配字符中，是否存在一段前缀，也同时是后缀？
                匹配了j个字符，那么next[j - 1]就是这j个字符自己的匹配长度
                前next[j-1]个字符匹配了，开始看他后一个跟pattern[i]匹不匹配
                """
                while j>0 and pattern[i] != pattern[j]:
                    j = next[j - 1]
                                    
                #如果匹配，前缀j长度加一
                if pattern[i] == pattern[j]:
                    j += 1

                next[i] = j
            
            return next
                
        next = build_next(needle)
        j = 0

        for i in range(len(haystack)):
            
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == len(needle):
                return i - j + 1
            
        return -1

## 注意
ord ^异或

## 复杂度
- 时间：O(m*n)
- 空间：O(1)

## 运行结果
- 执行用时：0 ms
- 内存消耗：17.43 MB 