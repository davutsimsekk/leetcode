class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def removezeros():
            while nums.count(0)!=0:
                nums.remove(0)
        removezeros()
        
        counter=0
        while len(nums)!=0:
            minimumu=min(nums)
            nums=list(map(lambda x: x-minimumu,nums))
            removezeros()
            counter+=1
        return counter