class Solution:
    def fib(self, n: int) -> int:
        def solve(n):
            
            if n==1:
                return 1
            elif n==0:
                return 0
            else:
                return solve(n-1)+solve(n-2)
        return solve(n)