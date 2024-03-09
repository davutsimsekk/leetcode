class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            while i<len(nums1) and j<len(nums2) and nums1[i]<nums2[j]:
                i+=1
            while i<len(nums1) and j<len(nums2) and nums1[i]>nums2[j]:
                j+=1
        return -1