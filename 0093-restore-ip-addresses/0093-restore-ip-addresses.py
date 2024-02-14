class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        finalres=[]
        def solve_greedy(num,counter,currindex,tmpres):
            nonlocal finalres
            if counter==4:
                if 0<=int(num)<=255:
                    finalres.append(".".join(tmpres))
                    return True
            else:
                for i in range(1,4):
                    try:
                        if counter!=3 and(0<=int(s[currindex:currindex+i])<=255) and (i==1 or s[currindex]!="0"):
                                    tmpres.append(s[currindex:currindex+i])
                                  
                                    solve_greedy(s[currindex:currindex+i],counter+1,currindex+i,tmpres)
                                    
                                    tmpres.pop()
                        else:

                            if 0<=int(s[currindex:])<=255 and (len(s[currindex:])==1 or s[currindex]!="0"):    
                                    tmpres.append(s[currindex:])
                                    solve_greedy(s[currindex:],counter+1,currindex+i,tmpres)
                                    tmpres.pop()
                    except:
                        continue        

        solve_greedy(s,0,0,[])
        return(list(set(finalres)))