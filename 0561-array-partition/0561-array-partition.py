class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        for i in range(len(nums)):
            if i%2==1:
                result+=nums[i-1]
        return result