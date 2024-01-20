class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str2)+1,0,-1):
            temp=str2[:i]
            if str2==(len(str2)//len(temp))*temp and str1==(len(str1)//len(temp))*temp:
                    return(temp)
        return("")