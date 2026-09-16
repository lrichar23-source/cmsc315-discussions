# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.

**Reflection**

This assignment gave me a much clearer picture of how graphs are represented in code and how traversal algorithms systematically 
explore them. I learned how an adjacency list models connections between nodes, and how a queue's FIFO behavior naturally 
produces BFS's level-by-level exploration pattern, since neighbors are always processed in the order they were discovered.
The main challenge was making sure nodes were marked as visited at the moment they were added to the queue, not when they 
were later processed. Marking them too late caused the same node to be added to the queue multiple times by different neighbors. 
I resolved this by tracing through the graph by hand, watching exactly when each node entered the visited set relative to 
when it entered the queue. Conceptually, BFS explores a graph outward in layers, visiting all nodes one step away before 
moving further, while DFS dives as deep as possible down one path before backtracking. This makes BFS ideal for finding 
the shortest path in unweighted graphs, such as routing in networks or finding the fewest connections between people in 
a social graph. DFS suits problems like maze-solving, detecting cycles, or exploring all possible paths, where depth 
matters more than proximity.
