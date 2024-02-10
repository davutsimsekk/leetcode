class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        sdict=dict()
        tdict=dict()
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]]=1
            else:
                sdict[s[i]]+=1
            if t[i] not in tdict:
                tdict[t[i]]=1
            else:
                tdict[t[i]]+=1
        if  t[-1] not in tdict:
            tdict[t[-1]]=1
        else:
            
            tdict[t[-1]]+=1 
        for i in t:
            if i not in sdict or sdict[i]!=tdict[i] :
                return i