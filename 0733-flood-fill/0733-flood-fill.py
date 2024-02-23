class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        value = image[sr][sc]

        if value==color:
            return image
        def check(row, col):
            image[row][col] = color
            if 0 <= row + 1 < len(image) and 0 <= col < len(image[0]) and image[row + 1][col] == value:
                check(row + 1, col)
            if 0 <= row - 1 < len(image) and 0 <= col < len(image[0]) and image[row - 1][col] == value:
                check(row - 1, col)
            if 0 <= row < len(image) and 0 <= col + 1 < len(image[0]) and image[row][col + 1] == value:
                check(row, col + 1)
            if 0 <= row < len(image) and 0 <= col - 1 < len(image[0]) and image[row][col - 1] == value:
                check(row, col - 1)
        check(sr,sc)
        return(image)