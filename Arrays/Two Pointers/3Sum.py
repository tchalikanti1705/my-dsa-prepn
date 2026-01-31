from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # STEP 1: Sort the array (Time: O(N log N))
        # Sorting is the key. It groups duplicates together and allows us
        # to use the Two-Pointer approach effectively.
        # Example: [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
        nums.sort()
        
        n = len(nums)
        answer = []

        # STEP 2: Iterate through the array to pick the first number ('i')
        for i in range(n):
            
            # OPTIMIZATION: Early Exit
            # Since the array is sorted, if nums[i] is positive (>0), 
            # we can't possibly add two other numbers to get 0.
            if nums[i] > 0:
                break
                
            # DUPLICATE CHECK (First Number)
            # If this number is the same as the previous one, we skip it
            # to avoid producing duplicate triplets.
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # STEP 3: The Two-Pointer Approach (Finding the other two numbers)
            # We are looking for: nums[lo] + nums[hi] = -nums[i]
            lo = i + 1      # Start just after 'i'
            hi = n - 1      # Start at the very end
            
            while lo < hi:
                current_sum = nums[i] + nums[lo] + nums[hi]
                
                # CASE A: Match Found!
                if current_sum == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    
                    # Now we must move pointers inward to find *other* pairs
                    # that might work with the same 'nums[i]'.
                    lo += 1
                    hi -= 1
                    
                    # DUPLICATE CHECK (Inner While Loops)
                    # These loops skip over identical numbers so we don't 
                    # get the same triplet twice. 
                    # NOTE: This looks like O(N^3), but because 'lo' and 'hi'
                    # never move backward, the whole loop logic is still O(N).
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                
                # CASE B: Sum is too small (< 0)
                # We need a larger number to reach 0. 
                # Since array is sorted, moving 'lo' to the right increases sum.
                elif current_sum < 0:
                    lo += 1
                
                # CASE C: Sum is too big (> 0)
                # We need a smaller number.
                # Moving 'hi' to the left decreases sum.
                else:
                    hi -= 1
                    
        return answer



'''
I solved 3Sum by combining sorting + fixed element + two pointers. First, I sort the array so duplicates come next to each other and so I can move pointers intelligently based on whether the sum is too small or too big. After sorting, I iterate over the array with an index i, treating nums[i] as the first number of the triplet. For each i, my goal becomes: find two numbers after i whose sum is -nums[i]. I also added an early stop: if nums[i] > 0, I break, because once the first number is positive in a sorted array, adding two more numbers will only make the sum bigger than zero.

For the remaining two numbers, I use the two-pointer method: lo = i+1 and hi = n-1. I compute current_sum = nums[i] + nums[lo] + nums[hi]. If the sum is 0, I store the triplet, move both pointers inward, and then skip duplicates on both sides so I don’t generate the same triplet again. If the sum is too small (negative), I move lo right to increase the sum; if the sum is too large (positive), I move hi left to decrease the sum. This works because sorting guarantees that moving pointers changes the sum in a predictable direction.

Time Complexity (TC): O(n²) — sorting costs O(n log n), then for each i you run a two-pointer scan that moves lo/hi across the array at most once, so overall it’s dominated by O(n²).
Space Complexity (SC): O(1) extra (ignoring the output) — you use constant extra variables; sorting may take extra space depending on the language implementation, and the answer list is output storage.
'''
