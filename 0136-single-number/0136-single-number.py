class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        dictionary=dict()
        for i in nums:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]+=1


        for i in range(len(dictionary)):
            if list(dictionary.values())[i]==1:
                return(list(dictionary.keys())[i])
                