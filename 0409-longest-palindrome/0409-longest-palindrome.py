class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictionary=dict()
        for i in s:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]+=1

        result=0
        is_encountered_one=False
        for i in dictionary.values():

            if is_encountered_one==False and i%2==1:
                result+=1

                is_encountered_one=True


            result=result+i//2
        if is_encountered_one==True:
            result=result*2-1
        else:
            result=result*2

        return(result)