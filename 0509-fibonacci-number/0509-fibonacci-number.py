class Solution:
    def fib(self, n: int) -> int:
        
        fiblist=[0,1]
        
#         def solve(n):
            
#             if n==1:
#                 return 1
#             elif n==0:
#                 return 0
#             else:
                
#                 return solve(n-1)+solve(n-2)
        def solve_opt(n):
            if n<=len(fiblist)-1:
                return fiblist[n]
            else:
                result= solve_opt(n-1)+solve_opt(n-2)
                fiblist.append(result)
                return result
        return solve_opt(n)