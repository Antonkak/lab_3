def bubble_sort(a: list[int]) -> list[int]:
    a = a[:]
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
def quick_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def counting_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    if min(a) < 0:
        raise ValueError("counting_sort only supports non-negative integers")
    max_val = max(a)
    count = [0] * (max_val + 1)
    for num in a:
        count[num] += 1
    result = []
    for i, freq in enumerate(count):
        result.extend([i] * freq)
    return result
def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if not a:
        return []
    negatives = [x for x in a if x < 0]
    positives = [x for x in a if x >= 0]

    def _radix_sort_nonneg(arr, base):
        if not arr:
            return arr
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            arr = _counting_sort_by_digit(arr, exp, base)
            exp *= base
        return arr

    def _counting_sort_by_digit(arr, exp, base):
        n = len(arr)
        output = [0] * n
        count = [0] * base
        for num in arr:
            index = (num // exp) % base
            count[index] += 1
        for i in range(1, base):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % base
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        return output

    sorted_pos = _radix_sort_nonneg(positives, base)
    sorted_neg = _radix_sort_nonneg([-x for x in negatives], base)
    sorted_neg = [-x for x in reversed(sorted_neg)]
    return sorted_neg + sorted_pos
def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    if not a:
        return []
    if buckets is None:
        buckets = len(a)

    min_val, max_val = min(a), max(a)
    if min_val == max_val:
        return a[:]
    normalized = [(x - min_val) / (max_val - min_val) for x in a]

    bucket_list: list[list[float]] = [[] for _ in range(buckets)]
    for x in normalized:
        idx = min(int(x * buckets), buckets - 1)
        bucket_list[idx].append(x)

    for bucket in bucket_list:
        n = len(bucket)
        for i in range(n):
            for j in range(n - 1 - i):
                if bucket[j] > bucket[j + 1]:
                    bucket[j], bucket[j + 1] = bucket[j + 1], bucket[j]
    result_normalized = []
    for bucket in bucket_list:
        result_normalized.extend(bucket)
    result = [x * (max_val - min_val) + min_val for x in result_normalized]
    return result
def heap_sort(a: list[int]) -> list[int]:
    a = a[:]
    n = len(a)

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

    return a
