class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited=set()
        row=col=0
        visited.add((row,col))
        for i in path:

            if i == "N":
                row+=1
                
            elif i=="S":
                row-=1
               
            elif i == "E":
                col+=1
                
            elif i == "W":
                col-=1
                
            if (row,col) in visited:
                return True
            else:
                visited.add((row,col))
        return False