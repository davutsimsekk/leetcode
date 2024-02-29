class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length=len(words)*len(words[0])
        wordict={}
        for i in words:
            if i not in wordict:
                wordict[i]=1
            else:
                wordict[i]+=1
        
        window=[]
        result=[]
        
        for i in range(len(s)-length+2):

            breaked=False
            seen=[]
            for j in words:
                if j not in seen and wordict[j]!=window.count(j):
                    breaked=True
                    break
                seen.append(j)
            if not breaked:
                result.append(i-1)
            window=[]
            for k in range(len(words)):
                window.append(s[i+k*len(words[0]):i+(k+1)*len(words[0])])

        return(result)