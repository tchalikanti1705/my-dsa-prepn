class Solution:
    def trap(self, height: List[int]) -> int:
        #the inution of the problem, lets take one bar thats i 0
        # now at 0th bar, if we have water then max it can store water depends on the 
        # left and right bars. and how much it can trap means min(l,r) and we have to minus
        # the original height 
        # so, formula will be min(lmx, rmax) - height[i]
        lp, rp = 0, len(height)-1
        lmax = 0
        rmax = 0
        ans = 0
        while lp<rp:
            lmax = max(lmax, height[lp])
            rmax = max(rmax, height[rp])
            if height[lp]<height[rp]:
                ans+= lmax - height[lp]
                lp+=1
            else:
                ans+= rmax - height[rp]
                rp-=1
        return ans




'''

I solved “Trapping Rain Water” using the two-pointer + running max approach. The main idea I used is: water trapped at any index depends on the tallest bar on its left and the tallest bar on its right. For each position i, the water it can hold is min(leftMax, rightMax) - height[i]. Instead of precomputing full leftMax/rightMax arrays, I tracked these two maximums while moving inward with two pointers.

I started with lp at the left and rp at the right. As I move, I keep updating lmax as the maximum height seen so far from the left, and rmax as the maximum height seen so far from the right. Then I decide which side to process: if the left bar is smaller than the right bar, I know the left side is the limiting side, so the trapped water at lp is determined by lmax (because there will always be some right boundary at least as tall as the current right bar). So I add lmax - height[lp] to the answer and move lp forward. Otherwise, I process the right side similarly by adding rmax - height[rp] and moving rp backward. Doing this repeatedly counts the trapped water for each bar exactly once.

Time Complexity (TC): O(n) — each pointer moves across the array at most once, so it’s a single linear pass.
Space Complexity (SC): O(1) — I only used a few variables (lp, rp, lmax, rmax, ans) and no extra arrays.



'''
