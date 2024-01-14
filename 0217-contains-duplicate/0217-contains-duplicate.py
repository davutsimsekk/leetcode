class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary=dict()
        for i in nums:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]+=1
        for i in dictionary.values():
            if i>=2:
                return True
        return False