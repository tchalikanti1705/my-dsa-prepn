class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1



'''



I solved “Move Zeroes” using a two-pointer in-place swap approach. I kept left as the index where the next non-zero number should be placed, and I used right to scan through the array from start to end. Every time I see a non-zero at nums[right], I swap it with nums[left] and then move left forward. This gradually pushes all non-zero elements to the front in their original relative order, and all the zeros naturally end up at the back because they get swapped behind the non-zeros.

Time Complexity (TC): O(n) — I scan the array once; each element is processed one time.
Space Complexity (SC): O(1) — I do everything in-place using swaps and only a pointer (left).

'''
