class Solution:
    def reverse(self, x: int) -> int:
        
        bosstr=""

        if str(x)[0]=="-":
            bosstr+="-"

        for i in reversed(str(x)):
            if i!="-":
                bosstr+=i

        if -2**31<int(bosstr)<=2**31 - 1:
            return(int(bosstr))
        else:
            return 0