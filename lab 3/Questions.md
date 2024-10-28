# 1/ What are the advantages and disadvantages of the recursive approach compared to the iterative approach?
=> 
# Advantages of Recursive Approach:
 Simplicity and Clarity:
    Recursive solutions can be more intuitive and easier to understand, especially for problems that have a natural recursive structure.
 Less Code:
    Most of the time it requires fewer lines of code, making them more brief.
# Disadvantages of Recursive Approach:
 Stack Overflow Risk:
    Deep recursion can lead to stack overflow errors if the recursion depth exceeds the call stack limit.
 Memory Usage: 
    Each recursive call consumes stack space, which can lead to higher memory usage compared to iterative solutions.
# Advantages of Iterative Approach:
 Efficiency: 
    Iterative solutions have better performance and lower memory overhead since they don't involve multiple function calls.
 No Stack Overflow Risk: 
    Iterative solutions can handle larger datasets without risking stack overflow.
# Disadvantages of Iterative Approach:
 Complexity:
    Some problems can be more complex to implement iteratively, leading to more verbose code that may be harder to understand.
 State Management:
    Iterative solutions often require explicit management of state, which can complicate the implementation.

# 2/How does memoization improve the performance of the recursive function? Are there any drawbacks?
=>
Memoization improve the performance of the recursive function by :-
    a. Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again. This significantly reduces the number of recursive calls, especially in problems with overlapping subproblems.
    b. By avoiding repeated calculations, memoization can reduce the time complexity of recursive algorithms from exponential to polynomial (like O(n) for memoized Fibonacci).
There are few drawbacks of memoization such as:-
Implementation Complexity:
  Implementing memoization can add complexity to the code if not handled carefully.
Overhead: 
  The overhead of storing and retrieving results can sometimes negate the performance benefits for certain problems with low complexity.

# 3/ In what scenarios might you prefer to use a generator function over other implementations?
=
Scenarios I prefere to use generator function are like when we want to control the flow of execution. Generator functions can be paused and resumed, which can is useful for implementing complex algorithms and for creating custom iterators. For example, we can use a generator function to implement a breadth-first search algorithm or a depth-first search algorithm.

# 4/ How does the space complexity differ between these implementations?
=
The space complexity differ between implementations as:
- As they yield one item at a time and does not store the entire sequence in memory.
- due to the call stack grows with each recursive call. Some lead to high memory usage for deep recursions.
- for simple iterative algorithms, they use a constant amount of space regardless of input size. More complex iterations have higher space complexity depending on the data structures used.
- Storing the results of computed states in addition to the O(n) space used by the call stack in the worst case.
- If the generator maintains state across iterations, the space used may vary based on the implementation.#