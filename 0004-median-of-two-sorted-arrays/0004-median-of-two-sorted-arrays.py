class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result=[]
        i,j=0,0
        while i!=len(nums1) and j!=len(nums2):
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i+=1

            else:
                result.append(nums2[j])
                j+=1

        while i<len(nums1):
            result.append(nums1[i])
            i+=1

        while j<len(nums2):
            result.append(nums2[j])
            j+=1
        if len(result)%2==1:
            return(result[len(result)//2])
        else:
            return (result[len(result)//2]+result[(len(result)//2)-1])/2