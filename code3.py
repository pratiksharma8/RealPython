def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        profit = max(profit, profit + diff)
    return profit


maxProfit([7, 1, 5, 3, 6, 4, 5, 8, 9, 6, 1])

