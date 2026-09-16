"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================
STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search (BFS): explores a graph level by level,
    visiting all of a node's immediate neighbors before moving on
    to neighbors of neighbors.

    Why a queue is used:
    A queue is First-In-First-Out (FIFO), which matches exactly how
    BFS needs to behave — the earliest-discovered nodes must be
    explored before newer ones. This guarantees nodes are visited in
    order of their distance from the start node (level by level).

    Why neighbors are added to the queue:
    When we visit a node, we don't process its neighbors immediately.
    Instead, we add them to the back of the queue so all nodes at the
    current level get processed before we move deeper into the graph.
    This is what creates the level-by-level traversal pattern.

    How BFS differs from depth-first traversal:
    DFS uses a stack (or recursion) and dives as deep as possible down
    one path before backtracking, exploring branch by branch. BFS
    instead spreads outward evenly, exploring all close neighbors
    before any distant ones — making it ideal for finding the
    shortest path in an unweighted graph.
    """
    # Handle a start node that doesn't exist in the graph
    if start not in graph:
        return []  # Nothing to traverse from a node that isn't there

    visited = set()       # Track visited nodes to avoid revisiting them
    visited.add(start)
    queue = deque([start])  # Queue manages the order nodes are processed
    order = []             # Records the order nodes were visited in

    while queue:
        current = queue.popleft()  # Remove from the front (FIFO order)
        order.append(current)

        # Visit each unvisited neighbor, marking it visited immediately
        # (not when it's later popped) to prevent it from being added
        # to the queue multiple times by different nodes.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Added to the back — explored later

    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # CREATE A GRAPH
    # ===============================
    print("\n=== GRAPH STRUCTURE ===")

    # Each key is a node (e.g., a person, city, or computer), and each
    # value is a list of nodes it's directly connected to. Think of
    # this as a small social network: nodes are people, and edges
    # represent friendships/connections between them.
    social_graph = {
        "Alice": ["Bob", "Carol"],
        "Bob": ["Alice", "David"],
        "Carol": ["Alice", "Eve"],
        "David": ["Bob", "Frank"],
        "Eve": ["Carol", "Frank"],
        "Frank": ["David", "Eve"],
    }

    print("Graph (adjacency list):")
    for node, neighbors in social_graph.items():
        print(f"  {node}: {neighbors}")
    # This graph has 6 nodes and multiple connections, including
    # some nodes with more than one edge, so BFS has real branching
    # decisions to make.

    # ===============================
    # BFS TRAVERSAL
    # ===============================
    print("\n=== BFS TRAVERSAL ===")

    start_node = "Alice"
    traversal_order = bfs(social_graph, start_node)
    print(f"Starting BFS from '{start_node}':")
    print(f"Traversal order: {traversal_order}")
    # BFS first visits Alice's direct neighbors (Bob, Carol) — level 1.
    # Then it visits THEIR unvisited neighbors (David, Eve) — level 2.
    # Finally it reaches Frank, who is connected to both David and Eve
    # — level 3. This demonstrates the "spreading outward" pattern:
    # everyone one step away is visited before anyone two steps away.

    # Adding an additional node/edge and re-running the traversal
    social_graph["Grace"] = ["Frank"]
    social_graph["Frank"].append("Grace")

    print("\nAdded new node 'Grace', connected to 'Frank'.")
    updated_order = bfs(social_graph, start_node)
    print(f"Updated traversal order: {updated_order}")
    # Grace is now reachable, but only through Frank, who is already
    # the farthest node from Alice. This pushes Grace out to the new
    # last level of the traversal, showing how BFS naturally extends
    # to cover new nodes without changing the earlier visiting order.

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Start from a different node
    print(f"\nBFS starting from 'Frank':")
    print(bfs(social_graph, "Frank"))
    # Starting from a different node produces a completely different
    # traversal order, since "distance" (number of hops) is measured
    # relative to whichever node we start from.

    # Edge case 2: Disconnected graph
    disconnected_graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
    }
    print(f"\nDisconnected graph: {disconnected_graph}")
    print(f"BFS starting from 'A': {bfs(disconnected_graph, 'A')}")
    # BFS only returns ['A', 'B'] — nodes C and D are never reached
    # because there's no edge connecting the two separate components.
    # BFS can only discover nodes that are reachable from the start.

    # Edge case 3: Missing start node
    print(f"\nBFS starting from missing node 'Zach':")
    print(bfs(social_graph, "Zach"))
    # Since "Zach" isn't a key in the graph at all, our function checks
    # for this case up front and returns an empty list instead of
    # crashing with a KeyError.

    # Edge case 4: Graph with only one node
    single_node_graph = {"Solo": []}
    print(f"\nSingle-node graph: {single_node_graph}")
    print(f"BFS starting from 'Solo': {bfs(single_node_graph, 'Solo')}")
    # With no neighbors to explore, BFS simply visits the start node
    # and immediately finishes, since the queue empties after just
    # one iteration.

    # Edge case 5: Empty graph
    empty_graph = {}
    print(f"\nEmpty graph: {empty_graph}")
    print(f"BFS starting from 'Anything': {bfs(empty_graph, 'Anything')}")
    # With no nodes at all, the start node can't exist in the graph,
    # so our guard clause immediately returns an empty list.


if __name__ == "__main__":
    main()