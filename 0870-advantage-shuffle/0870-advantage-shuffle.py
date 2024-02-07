class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)==1:
            return nums1
        snums1=sorted(nums1)
        snums2=sorted(nums2)
        dictionary=dict()
        
        while 0!=len(snums2):
            
            try:
                while snums2[0]>=snums1[0]:
                    
                    if snums2[-1] not in dictionary:
                        dictionary[snums2[-1]]=[snums1[0]]
                        snums2.pop(-1)
                        snums1.pop(0)
                    elif snums2[-1] in dictionary:
                        dictionary[snums2[-1]].append(snums1[0])
                        snums2.pop(-1)
                        snums1.pop(0)
                if snums2[0] not in dictionary:
                    dictionary[snums2[0]]=[snums1[0]]
                    snums2.pop(0)
                    snums1.pop(0)
                elif snums2[0] in dictionary:
                    dictionary[snums2[0]].append(snums1[0])
                    snums2.pop(0)
                    snums1.pop(0)
            except:
                pass
        result=[]
        for i in range(len(nums2)):
            
            result.append(dictionary[nums2[i]][-1])
            dictionary[nums2[i]].pop(-1)

        return(result)