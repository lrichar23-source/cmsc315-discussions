"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    Bubble Sort: repeatedly step through the list, comparing each
    pair of adjacent elements and swapping them if they're in the
    wrong order. Larger values "bubble up" toward the end of the
    list with each full pass.

    Time Complexity: O(n^2)
    Why: In the worst case, we make n passes through the list, and
    each pass compares up to n elements. This nested looping is what
    gives bubble sort its quadratic time complexity, making it
    inefficient for large datasets.
    """
    sorted_list = lst.copy()  # Work on a copy so the original list is untouched
    n = len(sorted_list)

    for i in range(n):
        swapped = False  # Track whether any swap happened this pass

        # After each pass, the largest unsorted element has "bubbled"
        # to its correct position at the end, so we can shrink the
        # range we still need to check (n - i - 1).
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap if the current element is bigger than the next one
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True

        # If no swaps occurred, the list is already sorted, so we can
        # stop early instead of doing unnecessary extra passes.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    Merge Sort: a divide-and-conquer algorithm. It recursively splits
    the list in half until each sublist has only one element (which
    is trivially "sorted"), then merges those sublists back together
    in sorted order.

    Time Complexity: O(n log n)
    Why: The list is divided in half at each level of recursion
    (log n levels), and merging all the pieces back together at each
    level takes O(n) time. Multiplying these gives O(n log n), which
    scales much better than bubble sort's O(n^2) on large datasets.
    """
    # Base case: a list of 0 or 1 elements is already sorted
    if len(lst) <= 1:
        return lst

    # Divide: split the list into left and right halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Conquer: recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Combine: merge the two sorted halves into one sorted list
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merge step: combine two already-sorted lists into a single
    sorted list by repeatedly comparing their front elements and
    appending the smaller one to the result.
    """
    result = []
    i = j = 0  # Pointers into left and right lists

    # Compare front elements of each list, appending the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements (only one of these will run,
    # since one list will already be exhausted by this point)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================
    print("\n=== DATASET #1 ===")

    data1 = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Original list: {data1}")

    bubble_result1 = bubble_sort(data1)
    print(f"Bubble Sort result: {bubble_result1}")

    merge_result1 = merge_sort(data1)
    print(f"Merge Sort result:  {merge_result1}")

    print(f"Original list unchanged: {data1}")
    # Both algorithms return a new sorted list without modifying the
    # original, and both produce identical, correctly sorted output —
    # confirming that different approaches can reach the same result.

    # ===============================
    # DATASET #2
    # ===============================
    print("\n=== DATASET #2 ===")

    data2 = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2]
    print(f"Original list: {data2}")

    bubble_result2 = bubble_sort(data2)
    print(f"Bubble Sort result: {bubble_result2}")

    merge_result2 = merge_sort(data2)
    print(f"Merge Sort result:  {merge_result2}")

    if bubble_result2 == merge_result2:
        print("Both algorithms produced identical sorted output.")
    # Even with a completely different dataset, both algorithms agree
    # on the correct sorted order, demonstrating that sorting
    # correctness doesn't depend on which algorithm is used — only
    # the efficiency of getting there differs.

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list
    empty_list = []
    print(f"\nEmpty list: {empty_list}")
    print(f"Bubble Sort: {bubble_sort(empty_list)}")
    print(f"Merge Sort:  {merge_sort(empty_list)}")
    # Both handle an empty list gracefully. Bubble sort's loops simply
    # never execute (range(0) is empty). Merge sort's base case
    # (len(lst) <= 1) catches this immediately and returns the empty
    # list as-is.

    # Edge case 2: Already sorted list
    already_sorted = [1, 2, 3, 4, 5]
    print(f"\nAlready sorted list: {already_sorted}")
    print(f"Bubble Sort: {bubble_sort(already_sorted)}")
    print(f"Merge Sort:  {merge_sort(already_sorted)}")
    # This is bubble sort's BEST case: since no swaps occur on the
    # first pass, the "swapped" flag stays False and the loop exits
    # early after just one pass — much faster than the worst case.
    # Merge sort still fully divides and re-merges the list regardless
    # of its initial order, so its performance doesn't change based on
    # how sorted the input already is.

    # Edge case 3: Reverse-sorted list
    reverse_sorted = [9, 7, 5, 3, 1]
    print(f"\nReverse-sorted list: {reverse_sorted}")
    print(f"Bubble Sort: {bubble_sort(reverse_sorted)}")
    print(f"Merge Sort:  {merge_sort(reverse_sorted)}")
    # This is bubble sort's WORST case: every element is out of order
    # relative to its neighbor, forcing the maximum number of swaps
    # and passes. Merge sort handles this with the same consistent
    # O(n log n) performance as any other input, since its efficiency
    # doesn't depend on the initial arrangement of the data.

    # Edge case 4: List with duplicate values
    duplicates = [4, 2, 4, 8, 2, 4, 1]
    print(f"\nList with duplicates: {duplicates}")
    print(f"Bubble Sort: {bubble_sort(duplicates)}")
    print(f"Merge Sort:  {merge_sort(duplicates)}")
    # Both algorithms handle duplicate values correctly, since equal
    # elements are simply left in their relative order (bubble sort
    # only swaps when strictly greater, and merge's "<=" comparison
    # keeps equal elements stable rather than needlessly swapping).

    # Edge case 5: Single-element list
    single = [42]
    print(f"\nSingle-element list: {single}")
    print(f"Bubble Sort: {bubble_sort(single)}")
    print(f"Merge Sort:  {merge_sort(single)}")
    # A single element is trivially "sorted." Bubble sort's inner loop
    # never runs since there's no adjacent pair to compare. Merge
    # sort's base case immediately returns the list without recursing
    # further.


if __name__ == "__main__":
    main()