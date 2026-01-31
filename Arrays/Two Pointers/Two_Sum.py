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
I solved “Two Sum” using a hash map lookup idea. First, I build a dictionary (hashmap) that stores each number as a key and its index as the value. Then I loop through the array again, and for every number nums[i], I compute the needed complement as target - nums[i]. If that complement exists in the hash map and it’s not the same index as i, I return the pair of indices [i, hashmap[compl]] immediately because I found two numbers that add up to the target.

Time Complexity (TC): O(n) — building the hashmap is O(n), and the second loop is O(n); hash lookups are O(1) average, so overall O(n).
Space Complexity (SC): O(n) — the hashmap can store up to n elements (one entry per number/index).

Quick note about this version: since you overwrite hashmap[nums[i]] = i, duplicates keep only the last index. It still works for most cases, but the more common cleaner version is a single-pass hash map (check complement first, then store current), which avoids the second loop and handles duplicates more naturally.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            compl = target - num
            if compl in hashmap:
                return [hashmap[compl], i]
            hashmap[num] = i
'''
