class Solution:
    def countDigits(self, num: int) -> int:
        stringnum=str(num)
        res=0
        for i in stringnum:
            if not num%int(i):
                res+=1
        return res