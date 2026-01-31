class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right]!=nums[right-1]:
                nums[left]=nums[right]
                left+=1
        return left




'''
I solved “Remove Duplicates from Sorted Array” using the two-pointer overwrite approach. Since the array is already sorted, all duplicates come next to each other. I keep a pointer left that represents the position where the next unique number should be placed, starting from index 1 (because the first element is always unique). Then I move right from index 1 to the end and compare nums[right] with nums[right-1]. If they are different, that means nums[right] is a new unique value, so I copy it into nums[left] and move left forward. By the end, the first left elements of the array are the unique values in order, and I return left as the count of unique elements.

Time Complexity (TC): O(n) — I scan the array once with right.
Space Complexity (SC): O(1) — I modify the array in-place and only use pointers (left, right).
'''
