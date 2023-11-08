class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        z=100
        i = 0
        if len(nums)==1:
                return 1
        
        while i < z-1:
            print(i)
            
            if nums[i] != nums[i + 1]:
                i += 1
            else:
                nums.pop(i)
            z = len(nums)
        print(nums)
        return len(nums)
        return nums
    