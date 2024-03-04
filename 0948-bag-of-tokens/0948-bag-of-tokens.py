class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res=0
        indexone = 0
        indextwo = len(tokens)-1
        while indexone<=indextwo:
            if power>=tokens[indexone]:
                power-=tokens[indexone]
                indexone+=1
                res+=1
            elif res>0:
                if indexone==indextwo:
                    indextwo-=1
                else:
                    power+=tokens[indextwo]
                    indextwo-=1
                    res-=1
            else:
                indextwo-=1
        return(res)