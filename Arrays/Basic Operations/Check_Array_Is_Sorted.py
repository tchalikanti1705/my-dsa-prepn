class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        if arr[0]>arr[-1]:
            return False
        i = 0
        j = 1
        while i<len(arr) and j<len(arr):
            if arr[i]<=arr[j]:
                i+=1
                j+=1
            else:
                return False
        return True



'''


Revision notes (how I solved it)

I solved this by checking the array pair by pair to confirm it is non-decreasing (sorted in ascending order). I first added a quick shortcut: if the first element is bigger than the last element, I immediately return False, because for an ascending sorted array the first should not be greater than the last.

Then I used two pointers i and j (starting at 0 and 1). I kept moving through the array and compared every adjacent pair: if arr[i] <= arr[j], that means the order is still valid, so I increment both pointers and continue. The moment I find any place where arr[i] > arr[j], I return False right away because that breaks the sorted property. If the loop completes without finding a violation, I return True.

Time Complexity (TC): O(n) — because I check each adjacent pair at most once in a single pass through the array.
Space Complexity (SC): O(1) — because I only use a couple of variables (i, j) and no extra data structures.

Small note: the early check arr[0] > arr[-1] is not needed (the pairwise checks already catch everything), but it doesn’t harm correctness for “sorted ascending” definition.


'''
