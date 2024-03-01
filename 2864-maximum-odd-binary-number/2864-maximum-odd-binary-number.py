class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        onenum=0
        res=""
        for i in s:
            if i=="1":
                onenum+=1
        for i in range(len(s)):
            if onenum>1:
                res="1"+res
                onenum-=1
            elif i==len(s)-1 and onenum==1:
                res=res+"1"
                return res
            else:
                res=res+"0"