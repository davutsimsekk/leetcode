class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sortdict=dict()
        for i,j in enumerate(order):
            
            sortdict[j]=i
            
        result=[s[0]]
        for i in s[1:]:
            if i in sortdict:
                index=0
                
                while index<len(result) and (result[index] not in sortdict or sortdict[i]>sortdict[result[index]]):
                    index+=1
                result.insert(index,i)
            else:
                result.append(i)
        return "".join(result)