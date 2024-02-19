class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i=0
        res=0
        indextwo=-1
        while i!=len(colors):
            if i==len(colors)-1 or colors[i]!=colors[i+1]:
                stack=neededTime[indextwo+1:i+1]
                res+=sum(stack)-max(stack)  
                indextwo=i
            i+=1
        return(res)