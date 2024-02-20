class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[]
        i=0
        for j in range(len(nums)):
            if j-i==2 and nums[j]-nums[i]<=k:
                res.append(nums[i:j+1])
                i=j+1
        if len(res)==len(nums)/3:
            return res
        else:
            return []