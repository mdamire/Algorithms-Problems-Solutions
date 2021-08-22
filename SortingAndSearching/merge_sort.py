"""
Complexity: O(n log n)
Evey iteration of input values takes O(log n) time as inputs gets half 
in size for every function call


Formula:
- create two subarrys of half size of input array
- merge the subarrys
"""

def merge_sort(n):
    """
    >>> merge_sort([2, 3, 1, 4, 2, 5, 6])
    [1, 2, 2, 3, 4, 5, 6]
    """
    k = len(n)//2

    if len(n) == 1:
        return n

    a = merge_sort(n[:k])
    b = merge_sort(n[k:])

    return merge(a, b)

def merge(a, b):
    r = []
    while a and b:
        if a[0] < b[0]:
            r.append(a[0])
            del a[0]
        else:
            r.append(b[0])
            del b[0]
    
    if a:
        r.extend(a)
    
    if b:
        r.extend(b)

    return r

if __name__ == "__main__":
    import sys
    r = merge_sort([int(i) for i in sys.argv[1:]])
    print(r)
