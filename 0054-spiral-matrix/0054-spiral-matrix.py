class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==1:
            return matrix[0]
        if len(matrix[0])==1:
            tmpres=[]
            for i in matrix:
                for j in i:
                    tmpres.append(j)
            return tmpres
        rownum=len(matrix)
        colnum=len(matrix[0])
        result=[]
        ust=0
        alt=len(matrix)-1
        sol=0
        sag=len(matrix[0])-1
        counter=0
        def solve_recursive(ust,alt,sag,sol,matrix):
            
            nonlocal counter
            row=ust
            col=sol
            while 0<=col<=sag:
                counter+=1
                result.append(matrix[row][col])
                col+=1
            if counter>=rownum*colnum:
                return True    
            col-=1
            row+=1
            while 0<=row<=alt:
                counter+=1
                result.append(matrix[row][col])
                row+=1
            if counter>=rownum*colnum:
                return True
            row-=1
            col-=1
            while 0<=col>=sol:
                counter+=1
                result.append(matrix[row][col])
                col-=1
            if counter>=rownum*colnum:
                return True
            col+=1
            row-=1
            while 0<=row>ust:
                counter+=1
                result.append(matrix[row][col])
                row-=1
            row+=1    
            if counter>=rownum*colnum:
                return True
            
            
            solve_recursive(ust+1,alt-1,sag-1,sol+1,matrix)
            

            
        solve_recursive(ust,alt,sag,sol,matrix)
        return(result)