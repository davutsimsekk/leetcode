class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and trust==[]:
            return 1
        dictionary=dict()
        guvenenler=[]
        for kisi,guven in trust:

                if guven not in dictionary:
                    dictionary[guven]=1
                else:
                    dictionary[guven]+=1
                guvenenler.append(kisi)
        for i in dictionary:
            if dictionary[i]==n-1 and i not in guvenenler:
                return i
        return -1