"""
Q: Find largest possible sum of a sequence of consecutive values is the array

A: The subarray that ends at k-1 position should also have the maximum sum.
"""

def max_subarray(arr):
    """
    >>> max_subarray([-1,2,4,-3,5,2,-5,2])
    11
    """
    
    maxsum = 0
    sum = 0
    for i in arr:
        sum = max(i, (i + sum))
        maxsum = max(maxsum, sum)

    print(maxsum)

if __name__ == "__main__":
    import sys
    max_subarray([int(i) for i in sys.argv[1:]])