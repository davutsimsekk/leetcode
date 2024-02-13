class Solution:
    def canJump(self, nums: List[int]) -> bool:

        index=len(nums)-1
        goldindex=len(nums)-1
        while index!=-1:
            if goldindex-index!=0 and nums[index]>=goldindex-index:
                goldindex=index
            index-=1
        if goldindex==0:
            return(True)
        else:
            return(False)