class Solution:
    def minPartitions(self, n: str) -> int:
        mini=0
        for i in n:
            if mini<int(i):
                mini=int(i)
            
        return mini