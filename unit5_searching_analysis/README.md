# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

I implemented a binary search tree application in Python by completing the TODO prompts in the starter file, adding 
explanatory comments to document my BST insertion and traversal operations, and committing my code with completed 
README documentation to GitHub. I analyzed binary search tree performance characteristics by explaining my design 
approach, reflecting on how trees improve performance compared to other data structures, describing scenarios where BSTs 
can become inefficient, and identifying a real-world application that demonstrates BST usage. I evaluated BST 
implementation quality by comparing my approach with at least two peers, analyzing how they handled edge cases 
(empty inputs, invalid operations, boundary conditions, insertion order effects, or tree shape variations), and 
suggesting specific improvements to efficiency, robustness, or usability.

**Reflection**

This assignment helped me understand how algorithmic efficiency is measured and why the same problem — finding a value 
in a list — can be solved in very different ways depending on the data's structure. Implementing linear search reinforced 
how a simple sequential scan works and why its time complexity is O(n): in the worst case, every element must be checked once. 
Implementing binary search taught me how sorted order enables a "divide and conquer" strategy, where comparing the target 
to the middle element eliminates half the remaining search space each iteration, producing O(log n) performance.
The main challenge was handling binary search's boundary conditions correctly — updating the low and high pointers 
so the loop terminates properly without skipping the target or looping infinitely. I resolved this by carefully tracing 
through small examples and testing edge cases like single-element and empty lists. In practice, linear search is best 
for small or unsorted datasets where sorting overhead isn't worth it, while binary search excels on large, sorted, 
and static datasets, since its logarithmic growth rate makes it dramatically faster as data scales — though it requires 
the added cost of maintaining sorted order.