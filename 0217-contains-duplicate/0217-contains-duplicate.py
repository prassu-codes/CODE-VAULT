class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool: 
        nums.sort()
        if len(nums)==1:
            return False
        else:
            for i in range(1,len(nums)):
                if nums[i]==nums[i-1]:
                    return True
            return False