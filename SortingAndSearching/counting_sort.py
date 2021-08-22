"""
Complexity: O(n)

Formula:
- a bookkeeping array is created whose indices are the elements of original array
- Can be used if the input element is small
"""

def counting_sort(n):
    b = [0] * (max(n) + 1) #Initialize bookkeeping array

    # Create bookkeeping array
    for i in n:
        b[i] += 1


    # Create result array from bookkeeping array
    r = [x for i in range(len(b)) if b[i] for x in [i] * b[i]]

    return r


#python3 counting_sort.py 3 55 10 100005 11 18 17 17 3 7 121 128
if __name__ == "__main__":
    import sys
    r = counting_sort([int(i) for i in sys.argv[1:]])
    print(r)