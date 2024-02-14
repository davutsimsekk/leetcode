class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        numresponse={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        finalres=[]
        def solve_recursive(index,tmpres):
            if index==len(digits):
                finalres.append("".join(tmpres))
                return True
            for i in numresponse[digits[index]]:
                tmpres.append(i)
                solve_recursive(index+1,tmpres)
                tmpres.pop()

        solve_recursive(0,[])
        return(finalres)