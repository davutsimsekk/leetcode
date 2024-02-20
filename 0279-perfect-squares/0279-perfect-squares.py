class Solution:
    def numSquares(self, n: int) -> int:
        squares=[]
        for i in range((int(n**0.5))+1):
            squares.append(i*i)
        

        dp=[float("inf")]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for j in reversed(squares):
                if i-j>=0:
                    dp[i]=min(dp[i],1+dp[i-j])
        return(dp[-1])