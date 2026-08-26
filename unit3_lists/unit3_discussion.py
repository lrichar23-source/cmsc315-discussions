"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""

def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.
    """
    # list.insert() shifts every element from `index` onward one position
    # to the right to make room for the new value. The list doesn't just
    # "add" the value in place -- everything after the insertion point
    # has to move over by one slot in memory.
    lst.insert(index, value)

    # Performance depends on WHERE the insertion happens:
    # - Inserting at the END (index == len(lst)) is O(1) on average, since
    #   no existing elements need to shift -- the value is just appended
    #   into free capacity at the back of the underlying array.
    # - Inserting at the BEGINNING or MIDDLE is O(n), because every element
    #   after the insertion point must be shifted right by one to preserve
    #   order. The closer to the front the insertion is, the more elements
    #   have to move.
    return lst


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.
    """
    # Validate the index BEFORE attempting to delete. Without this check,
    # calling lst.pop(index) or del lst[index] on an out-of-range index
    # would raise an IndexError and crash the program. Validating first
    # lets us fail safely and return a clear signal (None) instead.
    if index < 0 or index >= len(lst):
        print(f"  [!] Cannot delete: index {index} is out of range.")
        return None

    # pop(index) removes the value at that position and shifts every
    # element after it one position to the LEFT to fill the gap, similar
    # to how insertion shifts elements right. It also returns the removed
    # value so the caller can use or display it.
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    Search for a value within the list.
    """
    # This is a LINEAR search: we check each element one at a time,
    # starting from index 0, until we either find a match or reach the
    # end of the list. It's "linear" because the number of comparisons
    # grows directly (linearly) with the size of the list -- there's no
    # shortcut, since a plain Python list isn't sorted or indexed by value.
    for i in range(len(lst)):
        if lst[i] == value:
            return i  # Found it -- return the index immediately.

    # If the loop finishes without returning, the value isn't in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")

    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert at the beginning (index 0). This is the most expensive case
    # since every existing element must shift right.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning (index 0):", numbers)

    # Insert in the middle. Roughly half the elements shift right.
    middle_index = len(numbers) // 2
    insert_at(numbers, middle_index, 99)
    print(f"After inserting 99 in the middle (index {middle_index}):", numbers)

    # Insert at the end. Cheapest case -- no shifting required.
    insert_at(numbers, len(numbers), 100)
    print("After inserting 100 at the end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")
    print("Current list before deletions:", numbers)

    # Delete from the beginning.
    removed = delete_at(numbers, 0)
    print("Removed value from the beginning:", removed)
    print("  Updated list:", numbers)

    # Delete from the middle.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print(f"Removed value from the middle (index {middle_index}):", removed)
    print("  Updated list:", numbers)

    # Delete from the end.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed value from the end:", removed)
    print("  Updated list:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    print("Current list:", numbers)

    # Search for a value that exists.
    target = numbers[1] if len(numbers) > 1 else numbers[0]
    result = search_value(numbers, target)
    print(f"Searching for {target} (exists): found at index {result}")

    # Search for a value that does not exist.
    missing_target = 9999
    result = search_value(numbers, missing_target)
    print(f"Searching for {missing_target} (does not exist): result = {result}")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge case 1: delete using an invalid index.
    print("Attempting to delete at an invalid index (99):")
    delete_at(numbers, 99)

    # Edge case 2: search for a missing value (also covered above, but
    # shown again here explicitly as a dedicated edge case).
    print("Searching for a value guaranteed not to be present (-1):")
    result = search_value(numbers, -1)
    print("  Result:", result)

    # Edge case 3: insert into an empty list.
    empty_list = []
    print("Inserting into an empty list at index 0:")
    insert_at(empty_list, 0, "first_item")
    print("  List after insertion:", empty_list)

    # Edge case 4: delete from an empty list.
    truly_empty = []
    print("Attempting to delete from an empty list:")
    delete_at(truly_empty, 0)


if __name__ == "__main__":
    main()