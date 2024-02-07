class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix)
        for col in range(len(matrix)):
            matrix.append([])
            for row in range(len(matrix[0])-1,-1,-1):
                matrix[len(matrix)-1].append(matrix[row][col])

        for i in range(length):
            matrix.pop(0)