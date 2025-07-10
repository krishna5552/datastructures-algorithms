# datastructures-algorithms

To learn and practice DSA

## Data Structures

### Arrays (Lists)
- Initialization
- Access (by index)
- Update (by index)
- Traversal
- Insertion (at end)
- Insertion (at specific index)
- Deletion (from end)
- Deletion (from specific index)
- Searching (Linear)
- Searching (Binary)
- Resizing -- conceptual for python lists

### LinkedLists
- Node creation
- Initialization
- Insertion (at head)
- Insertion (at tail)
- Insertion (after a given node)
- Deletion (from head)
- Deletion (from tail)
- Deletion (of a specific node)
- Traversal
- Searching
- Reversal
- Cycle Detection

### Hash Tables (Hash Maps/Dictionaries & Hash Sets)
- Initialization
- Insertion / Add
- Deletion / Remove
- Lookup / Search / Get
- isEmpty
- Size
- Iteration

### Stacks
- Initialization
- Push
- Pop
- Peek / Top
- isEmpty
- Size

### Queues
- Initialization
- Enqueue
- Dequeue
- Peek / Front
- isEmpty
- Size

### Trees
- Node Creation
- For any binary tree (not necessarily sorted):
  - Traversal (In-Order)
  - Traversal (Pre-Order)
  - Traversal (Post-Order)
  - Traversal (Level-order / BFS)
  - Height / Depth Calculation
  - Counting Nodes
- For binary search trees specifically:
  - Search
  - Insertion
  - Deletion
  - Find minimum / maximum
  - Validation

---

## Searching & Sorting

### Searching
- Binary Search

### Sorting
- Merge Sort
- Quick Sort

---

## Patterns

### Two Pointers
**When to Suspect:**
- Problems involving **sorted arrays/lists** (finding pairs, triplets, specific sum, merging).
- Problems requiring **in-place modification** or rearrangement (moving elements, removing duplicates).
- Problems where you need to compare elements from **opposite ends** or maintain two distinct positions.

**Types of Two Pointers:**
- **Same Direction (Fast/Slow or Read/Write):** One pointer moves ahead (fast/read), the other (slow/write) moves only when a condition is met. Useful for removing duplicates, moving zeroes, cycle detection in linked lists.
- **Opposite Direction (Left/Right):** Pointers start at ends and move towards each other. Useful for finding pairs with a target sum in sorted arrays, reversing arrays/strings, finding palindromes, "Container With Most Water".

### Sliding Window
**When to Suspect:**
- Problems involving **contiguous subarrays or substrings**.
- Finding the **maximum/minimum sum/product** of a subarray of a certain size.
- Finding the **longest/shortest subarray/substring** that satisfies a condition.
- Often involves a "window" that expands and contracts.

**Techniques:**
- Usually involves two pointers (`left` and `right`) defining the window.
- Often uses a **hash map/frequency array** to keep track of elements *within* the current window.
- A `while` loop or `if` condition to shrink the window when a constraint is violated.

### Hash Map / Set Usage (Frequency, Lookup, Grouping)
**When to Suspect:**
- Problems asking about **frequencies or counts** of elements.
- Checking for **duplicates** or unique elements.
- Needing **O(1) average time lookups** to see if an element exists or what its associated value/index is.
- **Grouping** elements by a certain property (e.g., anagrams).
- Problems involving **"complements"** (e.g., `target - num`).

**Techniques:**
- Store `(element: count)`.
- Store `(element: index)`.
- Store just `element` (for sets).

### Sorting as a Preprocessing Step
**When to Suspect:**
- When the problem constraints are easier to handle if the data is ordered.
- When you need to find **adjacent elements** that satisfy a condition.
- When you can then apply **Two Pointers** or **Binary Search**.
- Problems asking for Kth smallest/largest, median, or range-based queries that benefit from order.

**Trade-off:** Adds O(N log N) time complexity and potentially O(N) space, but simplifies subsequent logic.

### Greedy Algorithms
**When to Suspect:**
- Optimization problems where making the **locally optimal choice at each step** leads to a globally optimal solution.
- Problems where you can build up the solution incrementally.
- Often applicable when there's a clear "best" immediate action.

**Challenge:** Proving correctness can be tricky; sometimes a greedy approach seems right but isn't.

### Recursion / Backtracking / DFS (Depth-First Search)
**When to Suspect:**
- Problems involving **trees or graphs** (traversals, finding paths, connectivity).
- Generating **permutations, combinations, subsets**, or exploring all possible paths/choices.
- Problems that can be broken down into smaller, similar sub-problems.

**Techniques:**
- **Base Case:** The condition that stops the recursion.
- **Recursive Step:** How the problem is broken down.
- **State Management:** Passing necessary information between recursive calls.
- **Pruning (for Backtracking):** Optimizing by abandoning paths that won't lead to a solution.

### Dynamic Programming (DP)
**When to Suspect:**
- **Optimization problems** (find max/min, count ways).
- Problems with **overlapping subproblems** (the same sub-problem is solved multiple times).
- Problems with **optimal substructure** (optimal solution to a problem can be constructed from optimal solutions of its sub-problems).
- Often involves sequences, paths, or grids.

**Techniques:**
- **Memoization (Top-Down):** Recursive solution with caching of results.
- **Tabulation (Bottom-Up):** Iterative solution building up results in a table.
- **Defining State:** What does `dp[i]` or `dp[i][j]` represent?
- **Recurrence Relation:** How to calculate `dp[i]` from previous `dp` values.

### Binary Search on Answer / Search Space
**When to Suspect:**
- When the problem asks for a **maximum of minimums** or **minimum of maximums**.
- When the answer lies within a **monotonic range**, and you can define a `check(X)` function that tells you if `X` is a *possible* answer.
- The actual array might not be sorted, but the *range of possible answers* is.

**Techniques:**
- Apply binary search not on array elements, but on the *range of possible answers*.


