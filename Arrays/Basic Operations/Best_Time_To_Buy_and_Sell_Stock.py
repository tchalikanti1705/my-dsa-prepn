class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #core idea two pointers, left is buying and right is for selling
        #if you do selling - buying (R-L) profit comes
        #if r<l that means we have smaller purchasing in future so, l=r
        #else keep left and move right for max profit
        left = 0
        profit = 0
        for right in range(1, len(prices)):
            profit = max(profit, prices[right]-prices[left])
            if prices[right]<prices[left]:
                left = right
        return profit




'''
I solved “Best Time to Buy and Sell Stock” using a clean one-pass two-pointer idea. I treat left as the day I’m buying (the cheapest price I’ve seen so far) and right as the day I’m selling (current day I’m checking). As I move right forward from day 1 to the end, I compute the profit if I bought at left and sold at right (prices[right] - prices[left]) and keep track of the maximum profit seen so far.

Whenever I find a price at right that is smaller than the current buying price (prices[right] < prices[left]), that means I found a better (cheaper) day to buy in the future, so I move left = right. Otherwise, I keep the same left and continue moving right, because a higher selling price later might give a bigger profit. At the end, profit contains the best possible single transaction profit, so I return it.

Time Complexity (TC): O(n) — I scan the array once with right and do O(1) work per step.
Space Complexity (SC): O(1) — I only use a few variables (left, profit) and no extra data structures.
'''
