class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # The Sudoku board is represented by a two-dimensional array. For each sub-array, we can check if the element already exists as a key in the hashmap. If not, then add them. If it's a '.', then we simply ignore it. If the number already exists in the hashmap, return false.

        #! The board is always guranteed to be 9x9, and board[i][j] is always a digit 1-9 or '.'.

        hashmap = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                # Construct keys for row, column, and box
                row_key = f"row_{i}_{val}"
                col_key = f"col_{j}_{val}"
                box_key = f"box_{(i // 3) * 3 + j // 3}_{val}"

                # Check for duplicates using the keys
                if row_key in hashmap or col_key in hashmap or box_key in hashmap:
                    return False
                
                # Add keys to hashmap
                hashmap[row_key] = True
                hashmap[col_key] = True
                hashmap[box_key] = True

        return True