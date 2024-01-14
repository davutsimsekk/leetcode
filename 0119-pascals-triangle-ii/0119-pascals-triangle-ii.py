class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1],[]]
        def solve(liste, index, row, numRows):
            if row==numRows:
                triangle.pop()
                return True
            if index==0:
                triangle[row+1].append(1)

            # Base Case
            if index == len(liste[row]) - 1:
                liste[row+1].append(1)
                triangle.append([])
                solve(liste, 0, row + 1, numRows)
                return True
            liste[row + 1].append(liste[row][index] + liste[row][index+1])
            solve(liste, index + 1, row, numRows)


        solve(triangle, 0,0,rowIndex)

        return(triangle[rowIndex])
