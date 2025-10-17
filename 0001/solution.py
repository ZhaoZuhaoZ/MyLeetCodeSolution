class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n,1):
                if nums[i]+nums[j] == target:
                    return [i, j]   
                
"""暴力解法
时间复杂度：O(n^2)
空间复杂度：O(1)
"""