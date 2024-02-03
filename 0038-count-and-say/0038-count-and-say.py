class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        result=""
        def solve(s,result):
            counter=1
            for i in range(len(s)):
                if i==len(s)-1:
                    result=result+f"{counter}"+f"{s[i]}"
                    
                    return result
                if s[i]!=s[i+1]:
                    result=result+f"{counter}"+f"{s[i]}"
                    counter=1
                    
                else:
                    counter+=1
            return(result)
        for i in range(n-1):
            s=solve(s,result)
        return(s)