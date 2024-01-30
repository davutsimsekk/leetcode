class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ortak_set=set(nums1).intersection(set(nums2))
        return [list(set(nums1)-ortak_set),list(set(nums2)-ortak_set)]