"""
Complexity: O(n^2)

Formula:
- if a < b and n[a] > n[b] (inversions) then swap(n[a], n[b]).
- For each iteration the largest value gets in the correct position
"""

def bubble_sort(n):
    """
    >>> bubble_sort([3,2,1])
    [1, 2, 3]
    >>> bubble_sort([1,5,3,5,6,2])
    [1, 2, 3, 5, 5, 6]
    """

    for i in range(len(n)):
        for j in range(len(n) - 1):
            if n[j] > n[j - 1]:
                (n[i], n[j]) = (n[j], n[i])


    return n

if __name__ == "__main__":
    import sys
    n = bubble_sort([int(i) for i in sys.argv[1:]])
    print(n)
