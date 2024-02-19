class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i=0
        res=0
        indextwo=-1
        while i!=len(colors):
            if i==len(colors)-1 or colors[i]!=colors[i+1]:
                stack=neededTime[indextwo+1:i+1]
                stack.sort()
                for j in range(len(stack)-1):
                    res+=stack[j]  
                indextwo=i
            i+=1
        return(res)