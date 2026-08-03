class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Step 1: Create 9 empty "baskets" for rows, columns, and boxes.
        # rows[i] will hold the digits already seen in row i
        # cols[j] will hold the digits already seen in column j
        # boxes[b] will hold the digits already seen in box b
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Step 2: Go through every cell in the 9x9 grid
        for i in range(9):          # i = row index (0 to 8)
            for j in range(9):      # j = column index (0 to 8)
                
                val = board[i][j]   # the value sitting at this cell

                # Step 3: Skip empty cells, nothing to check
                if val == ".":
                    continue

                # Step 4: Figure out which box this cell belongs to
                box_index = (i // 3) * 3 + (j // 3)

                # Step 5: Check if val already exists in this row, column, or box
                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False   # duplicate found -> invalid board

                # Step 6: Not a duplicate, so remember it for future checks
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)

        # Step 7: If we never hit a duplicate, the board is valid
        return True