"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time
import random


def linear_search(lst, target):
    """
    Linear search: check each element one at a time, in order,
    until the target is found or the list is exhausted.

    Time Complexity: O(n)
    Why: In the worst case (target is the last element, or not
    present at all), every single element in the list must be
    checked exactly once. There's no way to skip elements because
    linear search makes no assumptions about the list being sorted.
    On average, it checks about n/2 elements, but that's still
    proportional to n, so it's classified as O(n).
    """
    for index in range(len(lst)):
        # Compare the current element to the target
        if lst[index] == target:
            return index  # Found it — return its position immediately
    return -1  # Reached the end without finding it


def binary_search(lst, target):
    """
    Binary search: repeatedly divide the search space in half by
    comparing the target to the middle element. Requires the list
    to already be sorted.

    Time Complexity: O(log n)
    Why: Each comparison eliminates half of the remaining elements
    from consideration. Instead of checking one element at a time,
    we discard an entire half of the list with every step. This
    means the number of comparisons needed grows logarithmically
    with the size of the list, not linearly.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2  # Middle index of current search space

        if lst[mid] == target:
            return mid  # Found the target
        elif lst[mid] < target:
            # Target must be in the right half, so discard the left half
            low = mid + 1
        else:
            # Target must be in the left half, so discard the right half
            high = mid - 1

    return -1  # Search space shrank to nothing — target not present


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================
    print("\n=== SMALL DATASET TEST ===")

    small_data = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    print(f"Dataset: {small_data}")

    # --- Value that exists ---
    target_found = 45
    lin_result = linear_search(small_data, target_found)
    bin_result = binary_search(small_data, target_found)
    print(f"\nSearching for {target_found} (exists in list):")
    print(f"  Linear search result: index {lin_result}")
    print(f"  Binary search result: index {bin_result}")
    # Both algorithms correctly locate the value. On a small list like
    # this, the difference in speed is negligible to a human observer,
    # but binary search still uses fewer comparisons internally.

    # --- Value that does not exist ---
    target_missing = 100
    lin_result = linear_search(small_data, target_missing)
    bin_result = binary_search(small_data, target_missing)
    print(f"\nSearching for {target_missing} (does not exist):")
    print(f"  Linear search result: {lin_result}")
    print(f"  Binary search result: {bin_result}")
    # Both correctly return -1. Linear search had to check every
    # element to be sure, while binary search narrowed the range
    # down to nothing in just a few comparisons.

    # ===============================
    # LARGE DATASET
    # ===============================
    print("\n=== LARGE DATASET TEST ===")

    large_data = sorted(random.sample(range(1, 2_000_000), 1_000_000))
    target_found = large_data[750_000]   # Guaranteed to exist
    target_missing = -1                  # Guaranteed not to exist

    print(f"Dataset size: {len(large_data)} sorted elements")

    # --- Existing value timing ---
    start = time.perf_counter()
    lin_result = linear_search(large_data, target_found)
    lin_time = time.perf_counter() - start

    start = time.perf_counter()
    bin_result = binary_search(large_data, target_found)
    bin_time = time.perf_counter() - start

    print(f"\nSearching for an existing value:")
    print(f"  Linear search: index {lin_result}, time {lin_time:.6f}s")
    print(f"  Binary search: index {bin_result}, time {bin_time:.6f}s")

    # --- Missing value timing ---
    start = time.perf_counter()
    lin_result = linear_search(large_data, target_missing)
    lin_time = time.perf_counter() - start

    start = time.perf_counter()
    bin_result = binary_search(large_data, target_missing)
    bin_time = time.perf_counter() - start

    print(f"\nSearching for a missing value:")
    print(f"  Linear search: index {lin_result}, time {lin_time:.6f}s")
    print(f"  Binary search: index {bin_result}, time {bin_time:.6f}s")

    # As the dataset grows from ~10 elements to 1,000,000, linear
    # search's runtime grows roughly in proportion to the dataset
    # size (O(n)) — worst case it may check all 1,000,000 elements.
    # Binary search's runtime barely changes at all, since doubling
    # the dataset size only adds ONE more comparison (O(log n)).
    # log2(1,000,000) is about 20, meaning binary search never needs
    # more than ~20 comparisons no matter how large this list gets.
    # This gap becomes dramatically more visible as datasets scale up.

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list
    empty_list = []
    print(f"\nEmpty list: {empty_list}")
    print(f"  Linear search result: {linear_search(empty_list, 5)}")
    print(f"  Binary search result: {binary_search(empty_list, 5)}")
    # Both correctly return -1. Linear search's loop never executes
    # since range(0) is empty. Binary search starts with low=0,
    # high=-1, so low <= high is immediately False and the loop body
    # never runs.

    # Edge case 2: Single-element list
    single = [7]
    print(f"\nSingle-element list: {single}")
    print(f"  Linear search for 7: {linear_search(single, 7)}")
    print(f"  Binary search for 7: {binary_search(single, 7)}")
    print(f"  Linear search for 9: {linear_search(single, 9)}")
    print(f"  Binary search for 9: {binary_search(single, 9)}")
    # With one element, both algorithms just check that single item.
    # If it matches, index 0 is returned; otherwise -1.

    # Edge case 3: Target at the first position
    ordered = [1, 3, 5, 7, 9, 11]
    print(f"\nList: {ordered}")
    print(f"Target at first position (1):")
    print(f"  Linear search: {linear_search(ordered, 1)}")
    print(f"  Binary search: {binary_search(ordered, 1)}")
    # Linear search finds it immediately on the first check (best
    # case for linear search). Binary search still starts in the
    # middle and works its way down, so it may take a few more
    # comparisons even though the answer is at index 0.

    # Edge case 4: Target at the last position
    print(f"\nTarget at last position (11):")
    print(f"  Linear search: {linear_search(ordered, 11)}")
    print(f"  Binary search: {binary_search(ordered, 11)}")
    # This is linear search's worst case — it must scan through
    # every element before reaching the last one. Binary search
    # finds it in very few steps regardless of its position, since
    # position doesn't matter once the list is sorted.


if __name__ == "__main__":
    main()