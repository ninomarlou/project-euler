def main():
    x = number_spiral_diagonals(1001)
    print(x)


def number_spiral_diagonals(n):

    matrix = create_spiral_matrix(n)

    forward_diag_start = (n - 1, 0)
    back_diag_start = (0, 0)
    results = []
    for i in range(n):
        # forward_diag_start
        results.append(matrix[forward_diag_start[0]][forward_diag_start[1]])
        forward_diag_start = (
            forward_diag_start[0] - 1, forward_diag_start[1] + 1)
        # back_diag_start back_diag_start[0]
        results.append(matrix[back_diag_start[0]][back_diag_start[1]])
        back_diag_start = (back_diag_start[0] + 1, back_diag_start[1] + 1)

    return sum(list(dict.fromkeys(results)))


def create_spiral_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([0 for x in range(n)])
    return populate_matrix(n, matrix)


def populate_matrix(n, matrix):

    position = (0, n - 1)
    direction = 'left'
    cell_counter = n**2 - 1
    matrix[0][n - 1] = n**2

    while cell_counter > 0:
        # left
        if direction == "left":
            next_postion = next_move(position, (0, -1))
            if is_valid_move(next_postion, matrix):
                position = next_postion
                matrix[position[0]][position[1]] = cell_counter
                cell_counter -= 1
            else:
                direction = "down"
        if direction == "down":
            next_postion = next_move(position, (1, 0))
            if is_valid_move(next_postion, matrix):
                position = next_postion
                matrix[position[0]][position[1]] = cell_counter
                cell_counter -= 1
            else:
                direction = "right"
        if direction == "right":
            next_postion = next_move(position, (0, 1))
            if is_valid_move(next_postion, matrix):
                position = next_postion
                matrix[position[0]][position[1]] = cell_counter
                cell_counter -= 1
            else:
                direction = "up"
        if direction == "up":
            next_postion = next_move(position, (-1, 0))
            if is_valid_move(next_postion, matrix):
                position = next_postion
                matrix[position[0]][position[1]] = cell_counter
                cell_counter -= 1
            else:
                direction = "left"

    return matrix


def next_move(position, direction):
    return(position[0] + direction[0], position[1] + direction[1])


def is_valid_move(position, matrix):
    limit = len(matrix) - 1
    if position[0] < 0 or position[1] < 0:
        return False
    if position[0] > limit or position[1] > limit:
        return False
    if matrix[position[0]][position[1]] != 0:
        return False
    return True


if __name__ == "__main__":
    main()
