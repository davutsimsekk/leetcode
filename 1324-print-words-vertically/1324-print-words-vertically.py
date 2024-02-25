class Solution:
    def printVertically(self, s: str) -> List[str]:
        splited=s.split()
        result=[]

        maxlength=(max(map(len,splited)))


        for i in range(maxlength):
            tmp=""
            for j in range(len(splited)):
                
                try:
                    tmp+=(splited[j][i])
                except:
                    tmp+=" "
            result.append(tmp)
        
        for i in range(len(result)):
            result[i]=result[i].rstrip()
        return result