class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        result=0
        for i in range(len(colors)):
            for j in range(len(colors)-1,i,-1):
                if colors[i]!=colors[j]:
                    result=max(result,j-i)
                    break
        return result