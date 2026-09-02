# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

**What Was Completed**

All TODO sections were completed:

* List creation and basic operations (append, insert, remove, search, display) were implemented.
* Edge cases were handled: empty list operations, invalid indices, and single-element lists becoming empty.
* A real-world scenario demonstrating ordered list usage was created and run.
* Explanatory comments were added throughout the code.
* The program was tested to verify correct LIFO/FIFO-style ordering behavior where applicable and overall correctness.

I implemented a Python application that demonstrated list data structure usage by completing the TODO prompts in the 
starter file, running and verifying the functionality, and committing my documented code with explanatory comments to GitHub.
I analyzed list structure performance by describing when a linked list might outperform an array-based list, sharing a 
real-world scenario that uses a list data structure, and comparing my implementation approach with at least two peers, 
including edge case handling (empty inputs, invalid operations, boundary conditions, or performance constraints).
I evaluated list implementation quality by examining peer solutions, identifying differences in design approaches, 
and suggesting specific improvements to efficiency, robustness, or usability based on the requirements of the application scenario.


**Design approach**
My program implements three core list operations — insert_at, delete_at, and search_value — each wrapping Python's 
built-in list methods (insert(), pop(), and a manual linear scan) while adding validation and explanatory comments. 
I demonstrated the list's flexibility using a simple numeric dataset, inserting and deleting values at the beginning, 
middle, and end to show how position affects performance. I chose this generic numeric list because it makes the shifting 
behavior easy to observe directly in the printed output — you can watch the list reorganize itself after each operation, 
which makes the underlying mechanics concrete rather than abstract.
