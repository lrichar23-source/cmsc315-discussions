# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

**Reflection**

This assignment gave me hands-on practice with Python dictionaries and a deeper understanding of what's happening beneath 
their simple syntax. I learned how insertion, lookup, update, and deletion all rely on hashing keys to determine storage 
location, and how Python treats assignment as a dual-purpose operation — creating a new entry if the key is absent, or 
overwriting the value if it already exists. The main challenge was handling missing keys safely. Directly accessing or 
deleting a key that doesn't exist raises a KeyError, so I had to use .get() for safe lookups and an if key in dictionary 
check before deletion. Testing these edge cases helped me understand exactly when Python raises errors versus when it fails silently.
A hash table works by running each key through a hash function that converts it into a numeric index, telling the structure 
exactly where to store or retrieve that key's value. This gives average O(1) lookup time, since there's no need to scan 
every entry like a list would require. Collisions occur when two different keys hash to the same index; hash tables 
resolve this internally through techniques like chaining or open addressing, preserving efficiency even as more entries are added.
