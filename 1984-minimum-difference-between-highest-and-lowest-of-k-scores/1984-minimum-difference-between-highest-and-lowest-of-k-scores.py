class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        min_value=float("inf")
        for i in range(len(nums)-1):
            if i+k-1<len(nums):
                min_value=min(min_value,nums[i+k-1]-nums[i])
            
        return min_value