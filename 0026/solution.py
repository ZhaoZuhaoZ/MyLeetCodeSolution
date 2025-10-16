class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        fast = 1
        slow = 0

        while fast < n:
            if nums[fast] != nums[slow]:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        
        return slow + 1