class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrdict = dict()
        for i in arr:
            if i not in arrdict:
                arrdict[i] = 1
            else:
                arrdict[i] += 1

        sorteddict=(sorted(arrdict.items(),key=lambda x:x[1]))
        i=0
        counter=0
        while k>0:
            deger=sorteddict[i][1]
            if deger<=k:
                k-=deger
                counter+=1
            else:
                break
            i+=1

        return(len(sorteddict)-counter)