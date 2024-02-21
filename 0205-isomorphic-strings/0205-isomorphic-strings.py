class Solution:
    def isIsomorphic(self, s: str, t: str):
        
        if len(s)!=len(t):
            return False
        
        hashmap1=dict()
        hashmap2=dict()
        for i in range(len(s)):
            if s[i] in hashmap1:
                if hashmap1[s[i]]!=t[i]:
                    return False
                else:
                    continue
            else:
                hashmap1[s[i]]=t[i]
            if t[i] in hashmap2:
                if hashmap2[t[i]]!=s[i]:
                    return False
                else:
                    continue
            else:
                hashmap2[t[i]]=s[i]
    
        return True