Activity: Find the Time and Space Complexity
For each snippet, write the time complexity and space complexity using Big-O notation, and justify your answer in one line.

Snippet 1
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

Time complexity: O(n)      Space complexity: O(1)      Justify: The loop iterates through the array of length n once using constant extra space.

Snippet 2
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

Time complexity: O(n²)      Space complexity: O(1)      Justify: Nested loops compare all pairs of elements (up to n(n-1)/2 iterations) without extra memory.
Snippet 3
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

Time complexity: O(log n)      Space complexity: O(log n)      Justify: Dividng n by 10 in each recursive call yields depth proportional to the number of digits in n.
Snippet 4
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result

Time complexity: O(n²)      Space complexity: O(n²)      Justify: Two nested loops each run n times, storing n² total pairs in the result list.
Snippet 5
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

Time complexity: O(log n)      Space complexity: O(1)      Justify: Halves the search space in each iteration using constant auxiliary space.
Snippet 6
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result

Time complexity: O(n³)      Space complexity: O(n²)      Justify: Three nested loops run n times each, creating an n x n matrix for results.
Snippet 7
def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples

Time complexity (in terms of matrix dimensions m and n): O(m x n)      Space complexity (in terms of k non-zero elements): O(k)      Justify: Traverses all m x n cells and stores only the k non-zero elements in the list.
Snippet 8
def process(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])

Time complexity: O(n²)      Justify: Dominant n² operations from the nested loops outweigh the linear loop.
Snippet 9
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True
    return False

Time complexity: O(n)      Justify: Outer loop runs up to n times and inner loop runs constant 10 times.
Snippet 10
def reverse_new(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

Time complexity: O(n)      Space complexity: O(n)      Justify: Iterates backwards through array of length n while building a new array copy.
Snippet 11
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

Time complexity: O(n)      Space complexity: O(1)      Justify: Two-pointer approach performs n/2 swaps directly in place.
Snippet 12
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

Time complexity: O(n)      Space complexity: O(n)      Justify: Makes n recursive calls, building a call stack of depth n.
Snippet 13
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

Time complexity: O(2ⁿ)      Space complexity: O(n)      Justify: Each call splits into two recursive calls forming a binary tree of depth n.
Snippet 14
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count

Time complexity: O(n)      Space complexity: O(n)      Justify: Iterates through input array once with average O(1) set operations and stores up to n values.
Snippet 15
def print_all_subsets(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)

Time complexity: O(n · 2ⁿ)      Justify: Outer loop runs 2ⁿ times to construct all subsets, and inner loop checks n bit positions
Snippet 16
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

Time complexity: O(n + m)      Space complexity: O(n + m)      Justify: Single pass over both arrays of lengths n and m to store all elements in a merged result array.
Snippet 17
def is_palindrome(s):
    return s == s[::-1]

Time complexity: O(n)      Space complexity: O(n)      Justify: Slicing `s[::-1]` creates a reversed string copy of length n and compares each character.
Snippet 18
def flatten(matrix):
    flat = []
    for row in matrix:
        for val in row:
            flat.append(val)
    return flat

Time complexity (in terms of m rows and n columns): O(m · n)      Space complexity: O(m · n)      Justify: Visits every cell in the m x n grid and copies all elements into a 1D list.
Snippet 19
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

Time complexity: O(exp)      Space complexity: O(exp)      Justify: Decrements exp by 1 until 0, resulting in exp recursive stack frames.
Snippet 20
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base

Time complexity: O(log exp)      Space complexity: O(log exp)      Justify: Halves exp in each recursive call, creating log(exp) call stack levels.
Snippet 21
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False

Time complexity (in terms of the sizes of a and b): O(|a| · |b|)      Space complexity: O(1)      Justify: Nested loops iterate through each element pair in lists a and b without extra memory.
Snippet 22
def build_frequency_map(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq

Time complexity: O(n)      Space complexity: O(n)      Justify: Iterates over array of size n with O(1) dictionary lookups, storing up to n unique keys.
