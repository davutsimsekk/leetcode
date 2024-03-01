class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a_moves=[]
        b_moves=[]
        for i in range(len(moves)):
            if i%2==1:
                b_moves.append(moves[i])
            else:
                a_moves.append(moves[i])
        def check (row,col,moves):
            a=0
            for i in (moves):
                if i[0] == row:
                    a+=1
            if a==3:
                return True
            
            a=0
            for i in (moves):
                if i[1]==col:
                    a+=1
            if a==3:
                return True
            a=0
            b=0
            for i in range(3):
                if [i,i] in moves:
                    a+=1
                if [i,2-i] in moves:
                    b+=1  
            if a==3 or b==3:
                return True
            pass
        for i in a_moves:
            if check(i[0],i[1],a_moves):
                return "A"
        for i in b_moves:
            if check(i[0],i[1],b_moves):
                return "B"
        if len(moves)!=9:
            return "Pending"
        
        return "Draw"