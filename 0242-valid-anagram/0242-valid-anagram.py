class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        shash=dict()
        thash=dict()
        for i in range(len(s)):
            if s[i] not in shash:
                shash[s[i]]=1
            else:
                shash[s[i]]+=1
            if t[i] not in thash:
                thash[t[i]]=1
            else:
                thash[t[i]]+=1
        print(shash)
        print(thash)
        if shash==thash:
            return True
        return False