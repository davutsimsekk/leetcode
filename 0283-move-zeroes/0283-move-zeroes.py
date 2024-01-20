class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(nums.count(0)):
            for i in range (len(nums)-1):
                while nums[i]==0 and nums[i+1]!=0:
                    nums[i],nums[i+1]=nums[i+1],nums[i]  

