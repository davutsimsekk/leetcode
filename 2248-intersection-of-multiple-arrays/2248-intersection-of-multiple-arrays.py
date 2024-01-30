class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result=set(nums[0])
        for i in range(len(nums)-1):
            result=result & set(nums[i]) & set(nums[i+1])
            
        return sorted(result)