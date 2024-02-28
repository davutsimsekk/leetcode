class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                index_three=j+1
                index_four=len(nums)-1
                while index_three<index_four:
                    value=nums[i]+nums[j]+nums[index_three]+nums[index_four]
                    if value==target:
                        if [nums[i],nums[j],nums[index_three],nums[index_four]] not in result:
                            result.append([nums[i],nums[j],nums[index_three],nums[index_four]])
                        index_three+=1
                        index_four-=1
                    elif value<target:
                        index_three+=1
                    elif value>target:
                        index_four-=1
        
        return result