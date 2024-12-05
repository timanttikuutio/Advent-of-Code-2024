def bruteforce_scan(matrix):
    max_x = len(matrix[0]) - 1
    max_y = len(matrix) - 1

    total_score = 0

    for y in range(max_y+1):
        for x in range(max_x+1):
            # Check for right
            try:
                if matrix[y][x] == "X" and matrix[y][x+1] == "M" and matrix[y][x+2] == "A" and matrix[y][x+3] == "S":
                    total_score += 1
            except IndexError:
                pass

            # Check for left
            try:
                if matrix[y][x] == "X" and matrix[y][x-1] == "M" and matrix[y][x-2] == "A" and matrix[y][x-3] == "S":
                    total_score += 1
            except IndexError:
                pass

            # Check for up
            try:
                if matrix[y][x] == "X" and matrix[y-1][x] == "M" and matrix[y-2][x] == "A" and matrix[y-3][x] == "S":
                    total_score += 1
            except IndexError:
                pass


            # Check for down
            try:
                if matrix[y][x] == "X" and matrix[y+1][x] == "M" and matrix[y+2][x] == "A" and matrix[y+3][x] == "S":
                    total_score += 1
            except IndexError:
                pass

            # Check for diagonally positive right
            try:
                if matrix[y][x] == "X" and matrix[y+1][x+1] == "M" and matrix[y+2][x+2] == "A" and matrix[y+3][x+3] == "S":
                    total_score += 1
            except IndexError:
                pass

            # Check for diagonally negative right
            try:
                if matrix[y][x] == "X" and matrix[y-1][x+1] == "M" and matrix[y-2][x+2] == "A" and matrix[y-3][x+3] == "S":
                    total_score += 1
            except IndexError:
                pass

            # Check for diagonally positive left
            try:
                if matrix[y][x] == "X" and matrix[y+1][x-1] == "M" and matrix[y+2][x-2] == "A" and matrix[y+3][x-3] == "S":
                    total_score += 1
            except IndexError:
                pass

            # Check for diagonally negative left
            try:
                if matrix[y][x] == "X" and matrix[y-1][x-1] == "M" and matrix[y-2][x-2] == "A" and matrix[y-3][x-3] == "S":
                    total_score += 1
            except IndexError:
                pass



    return total_score


def main(testmode=False):
    with open("inputtest.txt" if testmode else "input.txt", "r") as file:
        matrix = []

        for row in file.readlines():
            matrix.append(list(row.strip()))

    print(bruteforce_scan(matrix))


if __name__ == '__main__':
    main(True)