"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================
    #
    # A Python dictionary IS a hash table under the hood. When a key
    # is added, Python runs the key through a hash function, which
    # converts it into a number. That number determines exactly where
    # in memory the key-value pair gets stored (its "bucket"). This is
    # why dictionaries can retrieve values so quickly — instead of
    # scanning every entry, Python computes the hash of the key we're
    # looking for and jumps almost directly to its location.

    print("\n=== INSERT OPERATIONS ===")

    inventory = {}  # Start with an empty dictionary (empty hash table)

    # Adding key-value pairs. Each key is hashed internally, and the
    # resulting hash determines where the pair is stored. Keys must be
    # unique and immutable (strings, numbers, tuples, etc.) because
    # the hash value depends on the key's contents never changing.
    inventory["apples"] = 50
    inventory["bananas"] = 30
    inventory["carrots"] = 75
    inventory["donuts"] = 12
    inventory["eggs"] = 24

    print("Dictionary after inserting 5 key-value pairs:")
    print(inventory)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================
    #
    # Looking up a value by key is fast (average O(1)) because Python
    # hashes the key we provide and goes straight to the bucket where
    # it should live, rather than checking every entry one by one like
    # a list would require.

    print("\n=== LOOKUP OPERATIONS ===")

    apple_count = inventory["apples"]
    print(f"Looking up 'apples': {apple_count}")
    # Python hashes "apples", finds the matching bucket, and returns
    # the value stored there directly.

    egg_count = inventory["eggs"]
    print(f"Looking up 'eggs': {egg_count}")
    # Same process — the hash of "eggs" points straight to its value,
    # with no need to scan through "apples", "bananas", etc. first.

    # ===============================
    # UPDATE OPERATIONS
    # ===============================
    #
    # Assigning a new value to an existing key does NOT create a new
    # entry. Python hashes the key, finds the existing bucket, and
    # simply overwrites the value stored there. The key itself and its
    # position in the hash table remain unchanged.

    print("\n=== UPDATE OPERATIONS ===")

    print(f"Before update: bananas = {inventory['bananas']}")
    inventory["bananas"] = 45  # Overwrites the existing value for this key
    print(f"After update:  bananas = {inventory['bananas']}")
    print(f"Full dictionary after update: {inventory}")

    # ===============================
    # DELETE OPERATIONS
    # ===============================
    #
    # Deleting a key removes both the key and its value from the hash
    # table entirely. The bucket that key occupied becomes free for
    # future insertions. Once deleted, the key no longer exists — any
    # future lookup for it will fail.

    print("\n=== DELETE OPERATIONS ===")

    print(f"Before deletion: {inventory}")
    del inventory["donuts"]
    print(f"After deleting 'donuts': {inventory}")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge case 1: Lookup a missing key
    # Using square-bracket access on a missing key raises a KeyError,
    # because there's no bucket to return a value from. Using .get()
    # instead lets us handle the missing key gracefully by returning
    # a default value (None, unless we specify otherwise).
    missing_lookup = inventory.get("grapes")
    print(f"Looking up missing key 'grapes' with .get(): {missing_lookup}")
    # Demonstrating the KeyError that direct access would raise:
    try:
        inventory["grapes"]
    except KeyError as e:
        print(f"Direct access inventory['grapes'] raised KeyError: {e}")

    # Edge case 2: Delete a missing key safely
    # Calling del on a key that doesn't exist raises a KeyError, so we
    # guard against it with a conditional check (or a try/except) to
    # delete safely without crashing the program.
    key_to_remove = "grapes"
    if key_to_remove in inventory:
        del inventory[key_to_remove]
        print(f"Deleted '{key_to_remove}'.")
    else:
        print(f"Tried to delete '{key_to_remove}', but it doesn't exist — "
              f"safely skipped instead of raising an error.")

    # Edge case 3: Update a missing key
    # Assigning a value to a key that doesn't exist yet doesn't cause
    # an error — Python simply creates a brand-new key-value pair.
    # This is different from update behavior on an existing key, where
    # only the value changes.
    print(f"\nBefore 'grapes' assignment: {inventory}")
    inventory["grapes"] = 20
    print(f"After assigning inventory['grapes'] = 20: {inventory}")
    # This shows that dictionaries don't distinguish between "update"
    # and "insert" at the syntax level — assignment does both,
    # depending on whether the key already exists.

    # Edge case 4: Use an empty dictionary
    empty_dict = {}
    print(f"\nEmpty dictionary: {empty_dict}")
    print(f"Length of empty dictionary: {len(empty_dict)}")
    print(f"Lookup on empty dict with .get(): {empty_dict.get('anything')}")
    # An empty dictionary behaves normally for all operations — lookups
    # simply find nothing, and .get() safely returns None rather than
    # raising an error. This confirms there's no special "broken" state
    # for an empty hash table; it's just a hash table with zero
    # occupied buckets so far.


if __name__ == "__main__":
    main()