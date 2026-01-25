class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_natural_nums = (n * (n+1))//2
        sum_of_arr = sum(nums)
        return sum_of_natural_nums - sum_of_arr


'''




I solved “Missing Number” using the sum formula trick. Since the array has n numbers taken from the range 0 to n with exactly one number missing, I first compute what the total sum should be if nothing was missing: n*(n+1)/2. Then I compute the actual sum of the given array using sum(nums). The missing number is simply the difference between these two sums, so I return expected_sum - actual_sum.

Time Complexity (TC): O(n) — because calculating sum(nums) scans the array once.
Space Complexity (SC): O(1) — because I only store a few variables (expected sum and actual sum), no extra data structures.





'''
