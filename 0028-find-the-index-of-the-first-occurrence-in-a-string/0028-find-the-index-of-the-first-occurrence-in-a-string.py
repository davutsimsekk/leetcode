class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        
        if haystack==needle:
            return 0
        
        indexone=0
        indextwo=indexone+len(needle)
        while indextwo!=len(haystack)+1:
            if needle in haystack[indexone:indextwo]:
                return indexone
            else:
                indexone+=1
                indextwo+=1
        return -1