class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        indexpos=0
        indexneg=0
        result=[]
        while indexneg<len(nums) and indexpos<len(nums):
            while nums[indexpos]<0:
                indexpos+=1
            while nums[indexneg]>0:
                indexneg+=1
            result.append(nums[indexpos])
            result.append(nums[indexneg])
            indexpos+=1
            indexneg+=1
        return(result)