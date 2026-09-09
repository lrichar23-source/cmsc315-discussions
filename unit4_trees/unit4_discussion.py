"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Each node stores one value, plus references to its
        # left and right children. A brand-new node has no
        # children yet, so both references start as None.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty tree simply has no root node yet.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Insertion depends on whether the new value is smaller or
        larger than the current node because that comparison is
        what keeps the tree "ordered": everything in a node's left
        subtree must be less than that node, and everything in its
        right subtree must be greater. Following that rule at every
        step is what lets us search in O(log n) time later, since
        each comparison eliminates half the remaining tree.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursive BST insertion.
        """
        # Base case: we've found an empty spot, so create a new
        # node here. This is where the value actually gets placed.
        if node is None:
            return Node(value)

        if value < node.value:
            # Smaller values always belong in the left subtree,
            # so we recurse left.
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger values always belong in the right subtree,
            # so we recurse right.
            node.right = self._insert_recursive(node.right, value)
        else:
            # Equal value: this is a duplicate. We choose to ignore
            # it and keep the tree unchanged (see EDGE CASES below).
            pass

        # Return the (possibly unchanged) node reference so the
        # parent call can reattach it correctly.
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        BST search is often more efficient than linear search
        (which is O(n)) because at each node we can rule out an
        entire half of the remaining tree just by comparing the
        target value to the current node's value. In a reasonably
        balanced tree, this gives O(log n) average-case search
        time instead of having to check every element one by one.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Recursive BST search.
        """
        if node is None:
            # We've fallen off the tree without finding the value.
            return False
        if value == node.value:
            return True
        elif value < node.value:
            # Target is smaller, so it can only be in the left subtree.
            return self._search_recursive(node.left, value)
        else:
            # Target is larger, so it can only be in the right subtree.
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        In-order traversal: left, current node, right.

        This order produces sorted output in a BST because of the
        same ordering property used during insertion: every value
        in a node's left subtree is smaller than the node, and
        every value in its right subtree is larger. By fully
        visiting the left subtree (all smaller values, in order)
        before visiting the node itself, and then fully visiting
        the right subtree (all larger values, in order) afterward,
        we naturally walk through every value from smallest to
        largest.
        """
        if node is None:
            return
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================
    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    # 50 becomes the root. Values smaller than the node they're
    # compared to go left (e.g., 30, 20, 40 end up in the left
    # subtree of 50), and values larger go right (e.g., 70, 60, 80
    # end up in the right subtree). Each insertion only has to
    # compare against nodes along one path from the root, so the
    # tree never has to look at the whole dataset to decide where
    # a value belongs — this is what makes BSTs efficient at
    # reducing the search space as they grow.
    for v in values_to_insert:
        tree.insert(v)
    print(f"Inserted values: {values_to_insert}")

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_values = tree.inorder()
    print(f"In-order traversal result: {sorted_values}")
    print("This is sorted because in-order traversal visits each")
    print("node's left subtree (smaller values) before the node")
    print("itself, and the right subtree (larger values) after.")

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    existing_values = [40, 80]
    missing_values = [15, 100]

    for v in existing_values:
        result = tree.search(v)
        print(f"Searching for {v}: {result} (value exists in the tree)")

    for v in missing_values:
        result = tree.search(v)
        print(f"Searching for {v}: {result} (value is not in the tree)")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge case 1: searching/traversing an empty tree.
    empty_tree = BST()
    print(f"Search in empty tree for 10: {empty_tree.search(10)}")
    print(f"In-order traversal of empty tree: {empty_tree.inorder()}")
    print("Both operations safely return False / an empty list")
    print("because the root is None, so the recursive helper")
    print("hits its base case immediately.")

    # Edge case 2: inserting a duplicate value.
    before = tree.inorder()
    tree.insert(50)  # 50 already exists in the tree
    after = tree.inorder()
    print(f"\nTree before inserting duplicate 50: {before}")
    print(f"Tree after inserting duplicate 50:  {after}")
    print("The tree is unchanged because our _insert_recursive")
    print("treats an equal value as a no-op instead of adding a")
    print("second node with the same value.")

    # Edge case 3: a tree with only one node.
    single_node_tree = BST()
    single_node_tree.insert(99)
    print(f"\nSingle-node tree in-order traversal: {single_node_tree.inorder()}")
    print(f"Search for 99: {single_node_tree.search(99)}")
    print(f"Search for 1: {single_node_tree.search(1)}")
    print("With only a root node, the recursive calls terminate")
    print("after checking that one node against the target value.")


if __name__ == "__main__":
    main()