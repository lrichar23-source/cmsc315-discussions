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

**Design approach**
My program implements three core list operations — insert_at, delete_at, and search_value — each wrapping Python's 
built-in list methods (insert(), pop(), and a manual linear scan) while adding validation and explanatory comments. 
I demonstrated the list's flexibility using a simple numeric dataset, inserting and deleting values at the beginning, 
middle, and end to show how position affects performance. I chose this generic numeric list because it makes the shifting 
behavior easy to observe directly in the printed output — you can watch the list reorganize itself after each operation, 
which makes the underlying mechanics concrete rather than abstract.
