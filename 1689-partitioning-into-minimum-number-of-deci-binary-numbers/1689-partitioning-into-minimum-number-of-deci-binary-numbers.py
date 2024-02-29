class Solution:
    def minPartitions(self, n: str) -> int:
        mini=0
        for i in n:
            mini=max(mini,int(i))
        return mini