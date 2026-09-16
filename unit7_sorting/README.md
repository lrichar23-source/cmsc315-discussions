# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

**Reflection**

This assignment strengthened my understanding of two very different approaches to solving the same problem — sorting a 
list. Implementing bubble sort reinforced how simple, nested iteration can produce correct results through repeated 
comparisons and swaps, while implementing merge sort deepened my understanding of recursion and the divide-and-conquer 
strategy, where a problem is broken into smaller pieces, solved independently, and recombined. The main challenge 
was writing the merge step correctly — making sure two already-sorted halves combined into one fully sorted list without 
losing or duplicating elements. I worked through this by tracing small examples by hand, tracking the two pointers 
as they moved through each half, which helped me see exactly when one list would be exhausted before the other. 
Bubble sort has O(n²) time complexity because it uses nested loops that compare every pair of elements, 
making it inefficient for large datasets, though it performs well on small or nearly-sorted data since it can exit early 
once no swaps occur. Merge sort consistently achieves O(n log n) performance regardless of the initial data order, making 
it far more scalable, though it requires additional memory to hold the split sublists during recursion. In practice, 
merge sort is preferable for large datasets, while bubble sort's simplicity suits small, simple teaching examples.