import pytest
from pathlib import Path
from src.lab2.sudoku import (
    is_valid_group,
    create_grid,
    group,
    get_row,
    get_col,
    get_block,
    find_empty_positions,
    find_possible_values,
    solve,
    check_solution,
    generate_sudoku,
)

@pytest.fixture
def sample_grid():
    return [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]

@pytest.fixture
def solved_grid():
    return [
        ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
        ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
        ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
        ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
        ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
        ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
        ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
        ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
        ['3', '4', '5', '2', '8', '6', '1', '7', '9']
    ]

def test_is_valid_group():
    assert is_valid_group(['1', '2', '3', '4', '5', '6', '7', '8', '9']) is True
    assert is_valid_group(['1', '2', '3', '4', '5', '6', '7', '8', '8']) is False
    assert is_valid_group(['1', '2', '3', '4', '5', '6', '7', '8', '.']) is True
    assert is_valid_group(['1', '1', '.', '.', '.', '.', '.', '.', '.']) is False

def test_create_grid():
    puzzle = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
    grid = create_grid(puzzle)
    assert len(grid) == 9
    assert len(grid[0]) == 9
    assert grid[0][0] == '5'
    assert grid[8][8] == '9'

def test_group():
    values = list(range(12))
    grouped = group(values, 3)
    assert grouped == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    with pytest.raises(ValueError):
        group(values, 5)

def test_get_row(sample_grid):
    assert get_row(sample_grid, (0, 0)) == sample_grid[0]
    assert get_row(sample_grid, (4, 3)) == sample_grid[4]

def test_get_col(sample_grid):
    assert get_col(sample_grid, (0, 0)) == ['5', '6', '.', '8', '4', '7', '.', '.', '.']
    assert get_col(sample_grid, (2, 8)) == ['.', '.', '.', '3', '1', '6', '.', '5', '9']

def test_get_block(sample_grid):
    assert get_block(sample_grid, (0, 0)) == ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    assert get_block(sample_grid, (4, 4)) == ['.', '6', '.', '8', '.', '3', '.', '2', '.']
    assert get_block(sample_grid, (8, 8)) == ['2', '8', '.', '.', '.', '5', '.', '7', '9']

def test_find_empty_positions(sample_grid, solved_grid):
    assert find_empty_positions(sample_grid) == (0, 2)
    assert find_empty_positions(solved_grid) is None

def test_find_possible_values(sample_grid):
    assert find_possible_values(sample_grid, (0, 2)) == {'1', '2', '4'}
    assert find_possible_values(sample_grid, (4, 4)) == {'5'}

def test_solve(sample_grid):
    solution = solve([row[:] for row in sample_grid])
    assert solution is not None
    assert check_solution(solution) is True

def test_check_solution(solved_grid):
    assert check_solution(solved_grid) is True
    solved_grid[0][0] = '1'
    assert check_solution(solved_grid) is False

def test_generate_sudoku():
    for N in range(10, 81, 10):
        grid = generate_sudoku(N)
        empty_count = sum(row.count('.') for row in grid)
        assert empty_count == 81 - N
        solution = solve([row[:] for row in grid])
        assert solution is not None
        assert check_solution(solution) is True
