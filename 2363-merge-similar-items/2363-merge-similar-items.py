class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashtable=dict()
        for i in items1:
            if i[0] not in hashtable:
                hashtable[i[0]]=i[1]
            else:
                hashtable[i[0]]+=i[1]
        for i in items2:
            if i[0] not in hashtable:
                hashtable[i[0]]=i[1]
            else:
                hashtable[i[0]]+=i[1]
        return sorted(list(hashtable.items()),key=lambda x:x[0])