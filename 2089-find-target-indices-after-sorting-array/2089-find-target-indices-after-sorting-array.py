class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]: 
        b=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                b.append(i)
        return b
        