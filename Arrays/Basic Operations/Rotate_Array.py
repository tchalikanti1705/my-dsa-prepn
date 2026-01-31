class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Step 1: reverse entire array
        reverse(0, n - 1)

        # Step 2: reverse first k elements
        reverse(0, k - 1)

        # Step 3: reverse remaining elements
        reverse(k, n - 1)


'''
I solved “Rotate Array” using the 3-reversal trick to rotate the array to the right by k steps in-place. First, I handle the empty array case, and then I reduce k using k %= n so I don’t do unnecessary full rotations when k is bigger than the array size. After that, I use a helper reverse(l, r) function that swaps elements from both ends inward to reverse a portion of the array.

The main idea is: if I reverse the whole array, the elements that need to come to the front (the last k elements) move to the beginning but in reversed order. So next, I reverse the first k elements to fix their order. Finally, I reverse the remaining n-k elements to fix their order too. After these three reversals, the array becomes exactly the right-rotated version.

Time Complexity (TC): O(n) — each reverse operation is linear, and across all three reversals the total work is proportional to n.
Space Complexity (SC): O(1) — everything is done in-place using swaps, only a few pointers/variables are used.
'''
