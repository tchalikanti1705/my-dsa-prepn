class Solution:
    def largest(self, arr):
        # code here
        mx = arr[0]
        for i in range(1,len(arr)):
            mx = max(arr[i], mx)
        return mx
'''
I solved the “largest element in an array” problem by doing a simple one-pass scan. First, I assumed the first element arr[0] is the maximum and stored it in a variable (like mx). Then I looped through the remaining elements from index 1 to the end. For every element, I compared it with mx, and if the current element was bigger, I updated mx to that value. By the time the loop finishes, mx holds the largest value in the entire array, so I return it. This approach is clean because it avoids sorting and just checks each element once.

SC: O(1)
TC: O(n)
'''
