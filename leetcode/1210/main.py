class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        # dp from the end
        cache = {}
        M = 100000000
        cache[(0, 0, True)] = M

        def dp(row, col, horizontal, count):
            key = (row, col, horizontal)
            if count >= cache[(0, 0, True)] or (key in cache and cache[key] <= count):
                return
            cache[key] = count
            if row == 0 and col == 0 and horizontal:
                return
            # up
            if (
                row > 0
                and not grid[row - 1][col]
                and (not horizontal or not grid[row - 1][col + 1])
            ):
                dp(row - 1, col, horizontal, count + 1)
            # left
            if (
                col > 0
                and not grid[row][col - 1]
                and (horizontal or not grid[row + 1][col - 1])
            ):
                dp(row, col - 1, horizontal, count + 1)
            # Flips
            if (
                horizontal
                and row < len(grid) - 1
                and not grid[row + 1][col]
                and not grid[row + 1][col + 1]
            ) or (
                not horizontal
                and col < len(grid[0]) - 1
                and not grid[row][col + 1]
                and not grid[row + 1][col + 1]
            ):
                dp(row, col, not horizontal, count + 1)

        dp(len(grid) - 1, len(grid) - 2, True, 0)
        return cache[(0, 0, True)] if cache[(0, 0, True)] != M else -1
