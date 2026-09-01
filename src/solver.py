#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    """
    alive_count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Checking all 8 adjacent directions using offsets
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            # Skiping the current cell itself
            if dr == 0 and dc == 0:
                continue
                
            r = row + dr
            c = col + dc
            
            # Ensuring that all the neighbors are within the grid boundaries
            if 0 <= r < rows and 0 <= c < cols:
                alive_count += grid[r][c]

    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Creating a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            
            # Rule 1 & 3: Underpopulation (<2) and Overpopulation (>3) cause death.
            # Rule 2: Survival (2 or 3) keeps a live cell alive.
            if grid[r][c] == 1:
                if neighbors == 2 or neighbors == 3:
                    next_grid[r][c] = 1
                else:
                    next_grid[r][c] = 0
                    
            # Rule 4: Reproduction (exactly 3) brings a dead cell to life.
            else:
                if neighbors == 3:
                    next_grid[r][c] = 1
                else:
                    next_grid[r][c] = 0

    return next_grid