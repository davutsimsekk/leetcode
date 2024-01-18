class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        number=nums.count(val)

        for i in range(number):
            nums.remove(val)

        return(len(nums))
