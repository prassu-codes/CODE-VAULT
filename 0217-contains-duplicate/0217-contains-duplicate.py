class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool: 
        p=set(nums)
        return len(p)!=len(nums)