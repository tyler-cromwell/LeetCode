class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = -1
        queue = []

        # Scan the matrix for all rotten oranges (2)
        rows = len(grid)
        cols = len(grid[0])
        initialBatch = set()
        for r in range(rows):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    initialBatch.add((r, c))
        queue.append(initialBatch)

        # Implement BFS
        while len(queue) > 0:
            # Get the current batch/layer of oranges
            batch = queue.pop(0)
            nextBatch = set()

            # Visit all oranges in the current batch, and add their neighbors to the next batch
            for r, c in batch:
                # Mark as visited (and rotted)
                grid[r][c] = -2
                
                # Get neighbors
                if (r-1) >= 0 and grid[r-1][c] == 1 and (r-1, c) not in batch:
                    nextBatch.add((r-1, c)) # Above
                if (r+1) < rows and grid[r+1][c] == 1 and (r+1, c) not in batch:
                    nextBatch.add((r+1, c)) # Below
                if (c-1) >= 0 and grid[r][c-1] == 1 and (r, c-1) not in batch:
                    nextBatch.add((r, c-1)) # Left
                if (c+1) < cols and grid[r][c+1] == 1 and (r, c+1) not in batch:
                    nextBatch.add((r, c+1)) # Right
            if len(nextBatch) > 0:
                queue.append(nextBatch)

            # Update minutes
            minutes += 1

        # Re-scan the grid to check for any unrotted oranges
        for r in range(rows):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1

        # Return minute count
        return minutes
