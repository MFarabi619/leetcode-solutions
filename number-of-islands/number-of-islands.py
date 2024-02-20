# Not my own solution. Inspired by Neetcode: https://www.youtube.com/watch?v=pV2kpPD66nE&ab_channel=NeetCode

# I added comments and learned the overall approach.

from typing import List
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty and return 0 if true.
        if not grid:
            return 0

        # Initialize the number of rows and columns.
        rows, cols = len(grid), len(grid[0])
        # Initialize a set to keep track of visited cells.
        visit = set()
        # Initialize the counter for islands.
        islands = 0

        # Define the BFS function to explore each island.
        def bfs(r, c):
            # Initialize a queue for BFS and add the starting cell.
            q = collections.deque()
            q.append((r, c))
            # Mark the starting cell as visited.
            visit.add((r, c))

            # Continue until the queue is empty.
            while q:
                row, col = q.popleft()
                # Define the directions to explore (up, down, left, right).
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Explore each direction from the current cell.
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Check if the new cell is within the grid bounds, is land, and hasn't been visited.
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visit
                    ):
                        # Add the new cell to the queue and mark it as visited.
                        q.append((r, c))
                        visit.add((r, c))

        # Iterate over each cell in the grid.
        for r in range(rows):
            for c in range(cols):
                # If the cell is part of land and hasn't been visited, perform BFS from this cell.
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    # After exploring the island, increment the islands counter.
                    islands += 1

        # Return the total number of islands found.
        return islands
