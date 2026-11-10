class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]: 
        p=[]
        for i in nums1:
            if i in nums2:
                p.append(i)
        q=list(set(p))
        return q
        