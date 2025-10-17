class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            num = nums[i]

            if target - num in hashtable:
                return [hashtable[target - num], i]
            
            # 不要提前插入，这样容易索引到自己
            hashtable[num] = i

        return []

"""哈希表解法
时间复杂度：O(n)
空间复杂度：O(n)
"""