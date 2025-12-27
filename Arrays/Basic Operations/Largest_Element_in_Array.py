class Solution:
    def largest(self, arr):
        # code here
        mx = arr[0]
        for i in range(1,len(arr)):
            mx = max(arr[i], mx)
        return mx
        
'''

1) What the problem is asking

You are given an array arr[].

You must find and return the largest (maximum) element in the array.

2) Basic cases (normal inputs)

Mixed numbers: [1, 8, 7, 56, 90] → 90

All equal: [5, 5, 5, 5] → 5

Single element: [10] → 10

3) Edge cases (important to remember)

Array with negative numbers: [-5, -2, -10] → -2 (your code works)

Array already sorted ascending/descending: works fine

Very large n: still fine because it’s one pass

Empty array: your code would crash at arr[0]

Usually GFG guarantees n >= 1, so it’s okay, but it’s a good edge case to remember in interviews.

4) Logic / Approach (what you did)

Start by assuming the first element is the largest: mx = arr[0]

Traverse from index 1 to end:

Update mx = max(mx, arr[i])

After the loop, mx is the largest value → return it

✅ This is the standard optimal approach (linear scan).

5) How your code is written (quick review)

Clean and readable.

Uses max() correctly.

Loop starts from 1, which avoids unnecessary comparison with itself.

Small improvement (optional):

Use a clearer name like max_val instead of mx (readability).

If handling general Python use-case, you could guard empty arrays.

6) Time Complexity (TC)

You scan the array once → O(n)

7) Space Complexity (SC)

Only one variable mx → O(1)

8) Alternative (Pythonic)

return max(arr)
Still O(n), but your manual scan is better for DSA practice/interview explanation.

'''