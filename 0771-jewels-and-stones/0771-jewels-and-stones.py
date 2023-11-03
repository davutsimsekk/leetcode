class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        
        output=0

        for i in stones:
            for a in jewels:
                if a==i:
                    output+=1

        return output
