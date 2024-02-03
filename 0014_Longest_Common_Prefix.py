class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimumu=(sorted(strs,key=len)[0])
        result=""
        for i in range(len(minimumu)):
            for j in strs:
                if minimumu[i]!=j[i]:
                       return result
            result+=minimumu[i]
            
        return result
