class Solution:
    def jump(self, nums: List[int]) -> int:
        lenght=len(nums)
        nums[lenght-1]=0
        for i in range(lenght-2,-1,-1):
            tmpmin=float("inf")
            for j in range(1,nums[i]+1):
                if i+j < len(nums):
                    tmpmin=min(tmpmin,nums[i+j])
            nums[i]=tmpmin+1
        return(nums[0])