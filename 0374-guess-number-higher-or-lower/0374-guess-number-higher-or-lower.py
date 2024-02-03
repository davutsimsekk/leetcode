class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        while True:
            mid=(r+l)//2
            tahmin=guess((r+l)//2)
            if tahmin>0:
                l=mid+1
            elif tahmin<0:
                r=mid-1
            else:
                return mid