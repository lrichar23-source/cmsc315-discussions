# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

**Reflection**

Completing this Binary Search Tree assignment deepened my understanding of recursion and how tree-based data structures 
organize information. I learned how recursive functions can elegantly handle insertion, search, and traversal by breaking 
each operation down into smaller subproblems — comparing a value, then delegating to the left or right subtree until a 
base case (an empty spot or a match) is reached. The main challenge was keeping track of how node references get updated 
during recursive insertion — specifically making sure each recursive call returns the updated subtree so the parent 
node's pointer is correctly reassigned. I overcame this by tracing through small examples by hand before writing code, 
which helped me visualize how the tree reconnects itself after each insertion. A BST's efficiency comes from its ordering 
property: every left child is smaller and every right child is larger than its parent. This means each comparison 
eliminates roughly half the remaining nodes from consideration, giving average-case O(log n) search and insertion — 
much faster than a linear list's O(n), where every element might need checking. Unlike arrays, a BST also avoids 
shifting elements when inserting, and unlike a plain linked list, it doesn't require checking every node sequentially.