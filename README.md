# leet-code pattern 

1. Prefix Sum:
   
   Involves preprocessing an array to create a new array where each element at index i represents the sum of the array from the start up to i.
   Use this pattern when you need to perform multiple sum queries on a subarray or need to calculate cumulative sums.

2. Two Pointers:
   
   Involves using two pointers to iterate through an array or list, often used to find pairs or elements that meet specific criteria.
   Use this pattern when dealing with sorted arrays or lists where you need to find pairs that satisfy a specific condition.
   
3. Sliding Window:
   
   Used to find a subarray or substring that satisfies a specific condition, optimizing the time complexity by maintaining a window of elements.
   Use this pattern when dealing with problems involving contiguous subarrays or substrings.

4. Fast & Slow Pointers:
   
   Used to detect cycles in linked lists and other similar structures.
   Initialize two pointers, one moving one step at a time (slow) and the other moving two steps at a time (fast).

5. LinkedList In-place Reversal:
   
   Pattern reverses parts of a linked list without using extra space.
   Use this pattern when you need to reverse sections of a linked list.

6. Monotonic Stack:

   Uses a stack to maintain a sequence of elements in a specific order (increasing or decreasing).
   Use this pattern for problems that require finding the next greater or smaller element.

7. Top 'K' Elements:

   Finds the top k largest or smallest elements in an array or stream of data using heaps or sorting.
   Use a min-heap of size k to keep track of the k largest elements.

8. Overlapping Intervals:

   Used to merge or handle overlapping intervals in an array.
   In an interval array sorted by start time, two intervals [a, b] and [c, d] overlap if b >= c.

9. Depth-First Search (DFS):
   
   Traverses as far down a branch as possible before backtracking.
   Useful for exploring all paths or branches in graphs or trees.

10. Breadth-First Search (BFS):

    Explores nodes level by level in a tree or graph.
    Helpful for finding shortest paths in unweighted graphs or level-order traversal.

11. Matrix Traversal:
    
    Involves traversing elements in a matrix using different techniques like DFS, BFS, etc.
    Useful for traversing 2D grids or matrices horizontally, vertically or diagonally.

12. Backtracking:
    
    Explores all possible solutions and backtracks when a solution path fails.
    Useful for finding all (or some) solutions to problems that satisfy given constraints.

13. Dynamic Programming Patterns:
    
    Involves breaking down problems into smaller subproblems and solving them using a bottom-up or top-down approach.
    Useful for problems with overlapping subproblems and optimal substructure.


    [!Important link](https://blog.algomaster.io/p/15-leetcode-patterns)