class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in hashmap and hashmap[compl]!=i:
                return [i, hashmap[compl]]
        return [-1, -1]





'''




I solved “Move Zeroes” using a two-pointer in-place swap approach. I kept left as the index where the next non-zero number should be placed, and I used right to scan through the array from start to end. Every time I see a non-zero at nums[right], I swap it with nums[left] and then move left forward. This gradually pushes all non-zero elements to the front in their original relative order, and all the zeros naturally end up at the back because they get swapped behind the non-zeros.

Time Complexity (TC): O(n) — I scan the array once; each element is processed one time.
Space Complexity (SC): O(1) — I do everything in-place using swaps and only a pointer (left).


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            compl = target - num
            if compl in hashmap:
                return [hashmap[compl], i]
            hashmap[num] = i



'''
