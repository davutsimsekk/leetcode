class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word2)!=len(word1):
            return False
        hash=dict()
        hash2=dict()
        for i in range(len(word1)):
            if word1[i] not in word2:
                return False
            if word1[i] not in hash:
                hash[word1[i]]=1
            else:
                hash[word1[i]]+=1
            if word2[i] not in word1:
                return False
            if word2[i] not in hash2:
                hash2[word2[i]]=1
            else:
                hash2[word2[i]]+=1
        
        return sorted((hash.values()))==sorted((hash2.values()))