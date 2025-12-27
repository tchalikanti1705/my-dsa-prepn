class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)<2:
            return -1
        mx1 = -1
        mx2 = -1
        
        for i in range(len(arr)):
            if arr[i]>mx1:
                mx2 = mx1
                mx1 = arr[i]
            elif arr[i]<mx1 and arr[i]>mx2:
                mx2 = arr[i]
        return mx2
        









'''



we solved this by scanning the array once and keeping track of the top two values while you go. Instead of sorting the array, you used two variables: mx1 to store the largest number seen so far, and mx2 to store the second largest distinct number seen so far.

While looping through the array, whenever you find a number bigger than mx1, you update mx2 to the old mx1 (because the previous largest now becomes the second largest), and then update mx1 to the current number. This way, mx1 always stays the largest so far.

If a number is not bigger than mx1, you still check whether it can become the second largest. You do that using the condition arr[i] < mx1 and arr[i] > mx2, which ensures the number is smaller than the largest (so it’s distinct) but larger than the current second largest. If it satisfies this, you update mx2.

Finally, you return mx2. If the array does not contain a second distinct largest value, mx2 remains -1, so returning it correctly matches the problem requirement. If negative numbers were allowed, we would initialize mx1 and mx2 differently instead of -1.



'''
