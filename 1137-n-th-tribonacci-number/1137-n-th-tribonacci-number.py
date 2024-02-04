class Solution:
    def tribonacci(self, n: int) -> int:
        calculated=[0,1,1]
        def solve(n):
            #BaseCase
            if n==0:
                return 0
            elif n==1 or n==2:
                return 1
            #RecursiveCase
            else:
                if len(calculated)>n:
                    return calculated[n]
                else:
                    value=solve(n-1)+solve(n-2)+solve(n-3)
                    calculated.append(value)
                    return value

        return solve(n)