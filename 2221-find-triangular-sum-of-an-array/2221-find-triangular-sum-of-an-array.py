class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def solve(newNums):
            if len(newNums)==1:
                return newNums[0]
            
            else:
                newnewNums=[]
                for i in range(len(newNums)-1):
                    newnewNums.append((newNums[i]+newNums[i+1])%10)
                return solve(newnewNums)
        return solve(nums)