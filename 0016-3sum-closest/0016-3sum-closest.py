class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float("inf")
        allvalues=float("inf")
        for k in range(len(nums)):
            indexOne=k+1
            indexTwo=len(nums)-1
            while indexOne<indexTwo:
                curr=nums[k]+nums[indexOne]+nums[indexTwo]
                if curr<target:
                    indexOne+=1
                else:
                    indexTwo-=1
                if allvalues>abs(target-curr):
                    allvalues=abs(target-curr)
                    closest=curr
        return(closest)