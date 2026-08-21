"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


from collections import deque


class Stack:
    def __init__(self):
        # Internal storage: a list holds the stack values.
        self._items = []

    def push(self, value):
        # Append adds to the END of the list. Since pop() also removes from
        # the end, the most recently added item is the first one out — LIFO.
        self._items.append(value)

    def pop(self):
        # Remove and return the most recently added value (top of the stack).
        # If the stack is empty, return None instead of raising an IndexError.
        if self.is_empty():
            print("  [!] Cannot pop: the stack is empty.")
            return None
        return self._items.pop()

    def peek(self):
        # Peek returns the top value WITHOUT removing it, so the caller can
        # inspect what's next without changing the stack.
        if self.is_empty():
            print("  [!] Cannot peek: the stack is empty.")
            return None
        return self._items[-1]

    def is_empty(self):
        # True when there are no values stored.
        return len(self._items) == 0

    def size(self):
        return len(self._items)


class Queue:
    def __init__(self):
        # Internal storage: deque allows efficient O(1) removal from the front.
        self._items = deque()

    def enqueue(self, value):
        # Append adds to the BACK of the queue. Since dequeue() removes from
        # the front, the first item added is the first one out — FIFO.
        self._items.append(value)

    def dequeue(self):
        # Remove and return the value at the FRONT of the queue.
        # If the queue is empty, return None instead of raising an error.
        if self.is_empty():
            print("  [!] Cannot dequeue: the queue is empty.")
            return None
        return self._items.popleft()

    def front(self):
        # Return the front value WITHOUT removing it — the next item to leave.
        if self.is_empty():
            print("  [!] Cannot view front: the queue is empty.")
            return None
        return self._items[0]

    def is_empty(self):
        # True when there are no values stored.
        return len(self._items) == 0

    def size(self):
        return len(self._items)


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
stack = Stack()

print("Pushing 4 values onto the stack: 10, 20, 30, 40")
for value in [10, 20, 30, 40]:
    stack.push(value)
print("Stack contents (bottom -> top):", stack._items)

print("Peek at the top value (not removed):", stack.peek())

# Demonstrate LIFO: values come off in reverse of insertion order.
print("Popping all values to show LIFO order:")
while not stack.is_empty():
    print("  Popped:", stack.pop())

# Edge case: pop and peek on an empty stack.
print("Attempting to pop from the now-empty stack:")
stack.pop()
print("Attempting to peek at the empty stack:")
stack.peek()

# Edge case: single item, remove it, verify empty.
print("Single-item test: push 99, then pop it.")
stack.push(99)
print("  Popped:", stack.pop())
print("  Is the stack empty now?", stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
queue = Queue()

print("Enqueuing 4 values into the queue: 'A', 'B', 'C', 'D'")
for value in ["A", "B", "C", "D"]:
    queue.enqueue(value)
print("Queue contents (front -> back):", list(queue._items))

print("View the front value (not removed):", queue.front())

# Demonstrate FIFO: values come out in the same order they went in.
print("Dequeuing all values to show FIFO order:")
while not queue.is_empty():
    print("  Dequeued:", queue.dequeue())

# Edge case: dequeue and front on an empty queue.
print("Attempting to dequeue from the now-empty queue:")
queue.dequeue()
print("Attempting to view the front of the empty queue:")
queue.front()

# Edge case: single item, remove it, verify empty.
print("Single-item test: enqueue 'Z', then dequeue it.")
queue.enqueue("Z")
print("  Dequeued:", queue.dequeue())
print("  Is the queue empty now?", queue.is_empty())

# ===============================
# REAL-WORLD SCENARIO
# ===============================
print("\n=== REAL-WORLD SCENARIO ===")

# Stack: browser back button. The last page you visit is the first
# one you return to when you hit "back."
print("Browser history (Stack / LIFO):")
history = Stack()
for page in ["home.html", "products.html", "cart.html"]:
    history.push(page)
    print("  Visited:", page)
print("  Pressing BACK returns to:", history.pop())
print("  Pressing BACK again returns to:", history.pop())

# Queue: print job spooler. Documents print in the order submitted.
print("\nPrinter job queue (Queue / FIFO):")
printer = Queue()
for job in ["Report.pdf", "Invoice.pdf", "Photo.png"]:
    printer.enqueue(job)
    print("  Submitted:", job)
print("  Printing first job:", printer.dequeue())
print("  Printing next job:", printer.dequeue())


if __name__ == "__main__":
    main()