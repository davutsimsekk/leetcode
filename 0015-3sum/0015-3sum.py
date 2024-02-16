class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 1):
            if i>0 and nums[i]==nums[i-1]:
                continue    
            pointer1 = i + 1
            pointer2 = len(nums) - 1
            while pointer1 < pointer2:   
                value=nums[i] + nums[pointer1] + nums[pointer2]
                if value == 0:
                    tmp=[nums[pointer2] ,nums[pointer1], nums[i]]
                    result.append(tmp)
                    pointer2-=1
                    while nums[pointer2+1]==nums[pointer2] and pointer1<pointer2:
                        pointer2-=1
                elif value<0:
                    pointer1+=1
                elif value>0:
                    pointer2-=1

        return result