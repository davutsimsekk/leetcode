class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index=0
        def binary_search(liste,index):

            if liste[len(liste)//2]==target:
                index+=len(liste)//2
                return(index)
                

            elif len(liste)==1:
                if liste[0]<target:
                    return(index+1)
                else:
                    return(index)

                
            elif liste[len(liste)//2]>target:

                return binary_search(liste[:len(liste)//2],index)
            else:
                index+=len(liste)//2
                return binary_search(liste[len(liste)//2:],index)
        return(binary_search(nums,index))