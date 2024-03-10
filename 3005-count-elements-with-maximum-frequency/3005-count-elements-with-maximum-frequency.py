class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter=dict()
        for i in nums:
            if i not in counter:
                counter[i]=1
            else:
                counter[i]+=1
        sirali_liste=list(reversed(sorted((counter.items()),key=lambda x:x[1])))
        mutekker=sirali_liste[0][1]
        res=0
        for i in range(len(sirali_liste)):
            if sirali_liste[i][1]==mutekker:
                res+=mutekker
        return res