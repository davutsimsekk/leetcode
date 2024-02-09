class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        lenght=len(nums)
        index=0
        counter=0
        for i in range(lenght-1):
            counter=0
            for j in range(lenght-1-i):
                nums.append((nums[index+j]+nums[index+j+1])%10)
                counter+=1
            index+=counter+1
        return nums[-1]