"""
Complexity: O(log n)
"""

def binary_search(n, x):
    a = 0
    b = len(n) - 1
    r = -1
    while a <= b:
        k = (a+b) // 2
        if n[k] == x:
            r = k
            break
        elif n[k] < x:
            a = k + 1
        else:
            b = k - 1

    return r

if __name__ == "__main__":
    r = binary_search([1,2,3,4,5,5,6,10,14,18,21], 10)
    print(r)
