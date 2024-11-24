from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        # Generate all perfect squares <= n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        # BFS setup
        queue = deque([(n, 0)])  # (remaining number, steps taken)
        visited = set()  # Track visited states to prevent cycles

        while queue:
            current, steps = queue.popleft()
            # Check all possible next states by subtracting a perfect square
            for square in squares:
                next_num = current - square
                if next_num == 0:  # Reached the goal
                    return steps + 1
                if next_num > 0 and next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, steps + 1))
        
        return -1  # If no solution is found (shouldn't happen per constraints)

# Time Complexity:
# - Generating perfect squares: O(sqrt(n)), as we compute all squares up to n.
# - BFS traversal: In the worst case, we visit all numbers from n to 0 -> O(n).
#   For each number, we try up to sqrt(n) perfect squares -> O(n * sqrt(n)).
# - Overall: O(n * sqrt(n)).

# Space Complexity:
# - Queue: At most O(n) states in the queue.
# - Visited set: At most O(n) unique states.
# - Perfect squares: At most O(sqrt(n)) squares stored.
# - Overall: O(n).
