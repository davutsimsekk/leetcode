class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        numdict=dict()
        
        for i in nums:
            if i not in numdict:
                numdict[i]=nums.count(i)
            else:
                continue
            if numdict[i]>len(nums)//2:
                return i