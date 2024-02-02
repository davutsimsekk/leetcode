class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows=[[] for i in range(numRows)]
        counter=0
        direction=True

        for i in s:
            if counter==0:
                direction=True
            
            elif counter==numRows-1:
                
                direction = False
            rows[counter].append(i)
            
            if direction:
                counter+=1
            else:
                counter-=1
        result=""
        for i in rows:
            for j in i:
                result+=j
        return(result)
