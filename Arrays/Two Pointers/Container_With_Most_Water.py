class Solution:
    def maxArea(self, height: List[int]) -> int:
        # here we need to find the max area of a container = width * height
        # the idea here is, lets take two heights say i, j, the width will be j-i
        # each unit is 1 width. and the height is min(h[i], h[j]) beacuse smaller the height, then that much it can store the water
        # and we move left or based based on the j value, because if i move the smaller value then i will encounter a bigger value in future becasue of that bigger value previous bigger value will become small and the area will be huge.
        res = 0
        lp, rp = 0, len(height)-1
        while lp<=rp:
            area = ((rp-lp) * (min(height[lp], height[rp])))
            res = max(res, area)
            if height[lp]<=height[rp]:
                lp+=1
            else:
                rp-=1
        return res






'''


I solved “Container With Most Water” using the classic two-pointer approach. I started with two pointers: lp at the left end and rp at the right end. For every pair (lp, rp), I compute the area as width × height, where width is (rp - lp) and height is the minimum of the two heights because water can only be held up to the smaller wall. I keep updating res with the maximum area found so far.

After calculating the area, I move the pointer that has the smaller height. The reason is: the current area is limited by the smaller wall, so keeping that smaller wall and only reducing width won’t help. The only chance to get a bigger area is to move past the smaller wall and hope to find a taller one, which can increase the limiting height even though width decreases. I repeat this until the pointers meet, and res ends up as the maximum possible container area.

Time Complexity (TC): O(n) — each pointer moves inward at most n times total, so it’s one linear pass.
Space Complexity (SC): O(1) — only pointers and a result variable are used.

Small code note: your loop condition can be while lp < rp (not <=). When lp == rp, width becomes 0 so area is 0 anyway; using < is the standard clean version.




'''
