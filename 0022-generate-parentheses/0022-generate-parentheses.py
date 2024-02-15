class Solution:
    def generateParenthesis(self, n: int):
        finalres=[]
        def solve_rec(tmpres,openednum):
            nonlocal finalres
            if len(tmpres)==n*2:
                if openednum==0:
                    finalres.append("".join(tmpres))
                return True
            for i in ("()"):
                if i==')' and openednum==0:
                    continue
                elif i=="(":  
                    tmpres.append("(")
                    solve_rec(tmpres,openednum+1)
                    
                    tmpres.pop()
                else:

                    tmpres.append(")")
                    solve_rec(tmpres,openednum-1)
                    tmpres.pop()
        solve_rec([],0)
        return finalres