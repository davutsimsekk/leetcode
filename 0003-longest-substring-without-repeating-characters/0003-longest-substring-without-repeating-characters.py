class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current=[]
        result=0
        if len(s)==1:
            return(1)
        for i in s:
            if i not in current:
                current.append(i)
                result=max(result,len(current))
            else:
                result=max(result,len(current))
                while i in current:
                    current.pop(0)
                current.append(i)

        return(result)