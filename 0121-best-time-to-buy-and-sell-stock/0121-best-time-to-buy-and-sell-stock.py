class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        indexone = 0
        indextwo = 1
        maxvalue=0
        while indextwo < len(prices):
            if prices[indexone] >= prices[indextwo]:
                indexone=indextwo
            else:
                maxvalue = max(prices[indextwo] - prices[indexone], maxvalue)
            indextwo+=1



        return(maxvalue)
