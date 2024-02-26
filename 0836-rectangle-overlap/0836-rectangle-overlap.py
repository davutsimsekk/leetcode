class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Check if rec2 is to the left of rec1
        if rec2[2] <= rec1[0]:
            return False
        # Check if rec2 is to the right of rec1
        if rec2[0] >= rec1[2]:
            return False
        # Check if rec2 is above rec1
        if rec2[3] <= rec1[1]:
            return False
        # Check if rec2 is below rec1
        if rec2[1] >= rec1[3]:
            return False
        # If none of the above conditions are true, then the rectangles overlap
        return True
