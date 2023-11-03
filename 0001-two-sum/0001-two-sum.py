class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        List=[]
        for i in range (0,len(nums)):
            for a in range (0,len(nums)):
                if nums[a]+nums[i]==target:
                    print(i,a)
                    if i!=a:    
                        List.append(i)
                        List.append(a)
                        return List
           