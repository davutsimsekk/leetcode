class Solution:
    def maxArea(self, height: List[int]) -> int:
        index_one=0
        index_two=len(height)-1
        result=0
        if len(height)==2:
            return min(height)

        while index_one<index_two:
            if height[index_one]<height[index_two]:
                
                result=max(result,min(height[index_one],height[index_two])*(index_two-index_one))
                index_one+=1
            else:
                
                result = max(result, min(height[index_one],height[index_two]) * (index_two - index_one))
                index_two-=1
        return result