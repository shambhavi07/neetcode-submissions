class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPointer=0
        maxProfit=0

        for sell in range(len(prices)):
            if prices[sell]< prices[buyPointer]:
                # that means no profit jump the buy to sell
                buyPointer= sell
            else:
                # we found a profit
                maxProfit= max(maxProfit, prices[sell]- prices[buyPointer])
        return maxProfit

        