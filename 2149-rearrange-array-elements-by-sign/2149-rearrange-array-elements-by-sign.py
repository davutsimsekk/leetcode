class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[]
        positives=[]
        posnum=0
        negatives=[]
        negnum=0
        for i in nums:
            if i>0:
                if negnum>0:
                    result.append(i)
                    result.append(negatives[0])
                    negatives.pop(0)
                    negnum-=1
                    continue
                posnum+=1
                positives.append(i)

            else:
                if posnum>0:
                    result.append(positives[0])
                    positives.pop(0)
                    result.append(i)
                    posnum-=1
                    continue
                negnum+=1
                negatives.append(i)
        return(result)