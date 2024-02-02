class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result=[]
        def solve(number):
            if str(number)[-1]=="0":
                return True
            else:
                if low<=number<=high:
                    result.append(number)
                solve(number*10+int(str(number)[-1])+1)

        for i in range(1,10):
            solve(i)
        return(sorted(result))