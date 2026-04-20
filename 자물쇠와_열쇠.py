from typing import List


def rotate_clockwise(matrix: List[List[int]]) -> List[List[int]]:
    size = len(matrix)
    return [[matrix[size - 1 - col][row] for col in range(size)] for row in range(size)]


def is_unlocked(expanded_lock: List[List[int]], lock_size: int) -> bool:
    for row in range(lock_size, lock_size * 2):
        for col in range(lock_size, lock_size * 2):
            if expanded_lock[row][col] != 1:
                return False
    return True


def apply_key(expanded_lock: List[List[int]], key: List[List[int]], x: int, y: int, delta: int) -> None:
    key_size = len(key)
    for row in range(key_size):
        for col in range(key_size):
            expanded_lock[x + row][y + col] += key[row][col] * delta


def solution(key: List[List[int]], lock: List[List[int]]) -> bool:
    lock_size = len(lock)
    board_size = lock_size * 3

    expanded_lock = [[0] * board_size for _ in range(board_size)]
    for row in range(lock_size):
        for col in range(lock_size):
            expanded_lock[row + lock_size][col + lock_size] = lock[row][col]

    current_key = key
    for _ in range(4):
        for x in range(lock_size * 2):
            for y in range(lock_size * 2):
                apply_key(expanded_lock, current_key, x, y, 1)
                if is_unlocked(expanded_lock, lock_size):
                    return True
                apply_key(expanded_lock, current_key, x, y, -1)

        current_key = rotate_clockwise(current_key)

    return False
