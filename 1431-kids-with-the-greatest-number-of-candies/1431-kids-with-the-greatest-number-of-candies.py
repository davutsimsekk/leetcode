class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxbebe=max(candies)
        result=[]
        for i in candies:
            if i+extraCandies>=maxbebe:
                result.append(True)
            else:
                result.append(False)

        return(result)