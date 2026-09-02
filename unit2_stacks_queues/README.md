# Unit 2 Discussion: Stacks and Queues

**Overview**

This assignment explored two fundamental linear data structures:

* Stack (LIFO)
* Queue (FIFO)

**Learning Objectives**

* Implemented stack operations
* Implemented queue operations
* Understood LIFO and FIFO behavior
* Created and tested edge cases

**What Was Completed**

All TODO sections were completed:

1. Stack operations were implemented using a Python list (end of list = top of stack).
2. Queue operations were implemented using collections.deque for efficient O(1) enqueue and dequeue.
3. LIFO behavior was demonstrated with a browser-history scenario (pages pushed and popped).
4. FIFO behavior was demonstrated with a print-spooler scenario (jobs enqueued and dequeued in arrival order).
5. Edge cases were tested: empty pop/peek/dequeue/front, and single-item structures becoming empty after removal.
6. Real-world scenarios (browser history and print queue) were created and run.

I implemented stack and queue data structures in Python by completing the TODO prompts in the starter file, adding explanatory 
comments to document my LIFO and FIFO operations, and committing my code with completed README documentation to GitHub.
I analyzed stack and queue behavior by explaining my design approach and how my application scenario demonstrated the 
use of these data structures, explaining why a stack uses LIFO and a queue uses FIFO with real-world use cases for each, 
and describing theoretically how memory usage grows as items are added to my structures.
I evaluated stack and queue implementations by comparing my approach with at least two peers, analyzing 
how they handled edge cases (empty inputs, invalid operations, boundary conditions, or performance constraints related 
to stack overflow or queue capacity), and suggesting specific improvements to efficiency, robustness, or usability.

**Reflection**
Working through this assignment reinforced how stacks and queues aren't just abstract structures — they mirror everyday 
sequencing problems like undo/redo, browser history, and task scheduling. I learned how choosing the right underlying 
container matters for performance: using deque for the queue instead of a plain list avoids the O(n) cost of removing 
from the front, which a list would incur by shifting every remaining element. My main challenge was handling edge cases 
cleanly — popping/dequeuing from an empty structure without crashing the program. I solved this by checking is_empty() 
before every removal and returning None with a clear message instead of letting an IndexError propagate. 
Testing the single-item case (push then pop, enqueue then dequeue) helped me confirm the "empty" state was tracked correctly 
rather than just assumed. The core difference between the two structures is order of access: a stack is LIFO, so the last 
thing added is the first thing removed, while a queue is FIFO, preserving insertion order. This distinction directly 
shapes which real-world problems each one models well.

**Design approach**
I used a browser back-button history as my stack scenario and a printer job spooler as my queue scenario, since both are 
situations most people intuitively understand. The stack fits browsing because reversing your most recent action 
(visiting a new page) is exactly what "back" does — it undoes the last step, not the first. The printer queue fits FIFO 
because fairness matters: the first document submitted should be the first one printed, regardless of what gets 
submitted afterward.
