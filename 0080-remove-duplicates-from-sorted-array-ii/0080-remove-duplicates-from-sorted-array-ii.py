class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        sayi_sayisi=1
        while i !=(len(nums)-1):
            if nums[i]==nums[i+1]:
                sayi_sayisi+=1
            else:
                sayi_sayisi=1

            if sayi_sayisi>2:
                nums.pop(i)
                i-=1
            i+=1

        return len(nums)