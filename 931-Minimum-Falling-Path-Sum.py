class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        finalresult=float("inf")
        cache={}
        def solve_min_sum(liste,row,col):
            #Base Case
            if row==len(matrix):
                return 0
            #Maybe Helper
            if col<0 or col==len(matrix):
                return float("inf")



            if (row,col) in cache:
                return cache[(row,col)]


            Result=matrix[row][col]+min(solve_min_sum(matrix,row+1,col+1),solve_min_sum(matrix,row+1,col),solve_min_sum(matrix,row+1,col-1))

            cache[(row,col)]=Result
            return Result

        for i in range(len(matrix[0])):
            finalresult=min(finalresult,solve_min_sum(matrix,0,i))
        return(finalresult)
