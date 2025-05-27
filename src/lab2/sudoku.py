import pathlib
import random
import time
import multiprocessing
import typing as tp

GridType = tp.List[tp.List[str]]
PosType = tp.Tuple[int, int]

def is_valid_group(group: tp.List[str]) -> bool:
    elements = [x for x in group if x != "."]
    return len(elements) == len(set(elements)) and all(e in "123456789" for e in elements)

def read_sudoku(path: tp.Union[str, pathlib.Path]) -> GridType:
    with pathlib.Path(path).open() as f:
        return create_grid(f.read())

def create_grid(puzzle: str) -> GridType:
    return group([c for c in puzzle if c in "123456789."], 9)

def display(grid: GridType) -> None:
    line = "+".join(["-" * 6] * 3)
    for row in range(9):
        print("".join(
            grid[row][col].center(2) + ("|" if col in {2, 5} else "")
            for col in range(9)
        ))
        if row in {2, 5}:
            print(line)

def group(values: tp.List[tp.Any], n: int) -> tp.List[tp.List[tp.Any]]:
    if len(values) % n != 0:
        raise ValueError("Cannot group values into equal parts")
    return [values[i:i + n] for i in range(0, len(values), n)]

def get_row(grid: GridType, pos: PosType) -> tp.List[str]:
    return grid[pos[0]]

def get_col(grid: GridType, pos: PosType) -> tp.List[str]:
    return [grid[r][pos[1]] for r in range(9)]

def get_block(grid: GridType, pos: PosType) -> tp.List[str]:
    br, bc = 3 * (pos[0] // 3), 3 * (pos[1] // 3)
    return [grid[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]

def find_empty_positions(grid: GridType) -> tp.Optional[PosType]:
    for r in range(9):
        for c in range(9):
            if grid[r][c] == ".":
                return r, c
    return None

def find_possible_values(grid: GridType, pos: PosType) -> tp.Set[str]:
    used = set(get_row(grid, pos)) | set(get_col(grid, pos)) | set(get_block(grid, pos))
    return set("123456789") - used

def solve(grid: GridType) -> tp.Optional[GridType]:
    pos = find_empty_positions(grid)
    if not pos:
        return grid

    r, c = pos
    for val in find_possible_values(grid, pos):
        grid[r][c] = val
        if solve(grid):
            return grid
        grid[r][c] = "."
    return None

def check_solution(solution: GridType) -> bool:
    for i in range(9):
        if not (
            is_valid_group(solution[i]) and
            is_valid_group([solution[r][i] for r in range(9)]) and
            is_valid_group([
                solution[r][c]
                for r in range(3 * (i // 3), 3 * (i // 3) + 3)
                for c in range(3 * (i % 3), 3 * (i % 3) + 3)
            ])
        ):
            return False
    return True

def generate_sudoku(N: int) -> GridType:
    grid = [["." for _ in range(9)] for _ in range(9)]
    solution = solve([row[:] for row in grid])
    if not solution:
        return grid

    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    for r, c in positions[:81 - min(N, 81)]:
        solution[r][c] = "."

    return solution

def run_solve(file_name: str) -> None:
    grid = read_sudoku(file_name)
    start = time.time()
    solution = solve(grid)
    elapsed = time.time() - start

    print(f"{file_name}: {'Solved' if solution else 'No solution'} in {elapsed:.3f} sec")
    if solution:
        print("Solution is valid" if check_solution(solution) else "Invalid solution")

if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        p = multiprocessing.Process(target=run_solve, args=(fname,))
        p.start()
