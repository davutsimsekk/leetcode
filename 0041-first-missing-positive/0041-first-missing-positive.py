class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        j=1
        nums=list(set(nums))
        nums.sort()
        while True:
            if i==len(nums):
                return j
            if nums[i]<=0:
                i+=1
                continue
            if j!=nums[i] :
                return j
            else:
                j+=1
                i+=1