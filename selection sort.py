# Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.
# Example 1:
#
# Input:
# N = 5
# arr[] = {4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9
# Explanation:
# Maintain sorted (in bold) and unsorted subarrays.
# Select 1. Array becomes 1 4 3 9 7.
# Select 3. Array becomes 1 3 4 9 7.
# Select 4. Array becomes 1 3 4 9 7.
# Select 7. Array becomes 1 3 4 7 9.
# Select 9. Array becomes 1 3 4 7 9.
# Complete the functions select() and selectionSort(), where select() takes
# arr[] and starting point of unsorted array i as input parameters and returns theselected element
# for each iteration in selection sort, and selectionSort() takes the array and it's size and sorts the array.
class Solution:
    def select(self, arr, i):
        n = len(arr)
        minIndex = i
        for j in range(i+1,n):
            if arr[j]<arr[minIndex]:
                minIndex = j
        return minIndex
    def selectionSort(self, arr, n):
        for i in range(n-1):
            minIndex = self.select(arr,i)
            arr[i],arr[minIndex] = arr[minIndex],arr[i]

# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends