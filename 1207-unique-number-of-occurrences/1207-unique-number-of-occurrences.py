class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash=dict()
        for i in arr:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
        return len(list(hash.values()))==len(set(hash.values()))