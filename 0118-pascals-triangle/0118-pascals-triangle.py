class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1],[]]
        def solve(liste, index, row, numRows):
            if row==numRows:
                liste.pop()
                return True
            if index==0:
                liste[row+1].append(1)

            # Base Case
            if index == len(liste[row]) - 1:
                liste[row+1].append(1)
                liste.append([])
                solve(liste, 0, row + 1, numRows)
                return True
            liste[row + 1].append(liste[row][index] + liste[row][index+1])
            solve(liste, index + 1, row, numRows)

        solve(triangle, 0,0,numRows-1)
       
        return(triangle)