class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result=0
        for indexone in range(len(nums)-1):
            for j in range(indexone+1,len(nums)):
                if nums[indexone]+nums[j]<target:
                    result+=1    
        return result
                