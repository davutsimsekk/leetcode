class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        result=[]
        number=1
        n=1
        while number!=9:
            if n==10:
                n=1
                number=int(str(number)[0])+1
            if str(number)[-1]!=str(n-1):
                n+=1
            else:
                number=number*10+n
                if low<=number<=high:
                    result.append(number)

        return(sorted(result))