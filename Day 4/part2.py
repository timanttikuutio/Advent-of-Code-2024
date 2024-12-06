def bruteforce_scan(matrix):
    max_x = len(matrix[0]) - 1
    max_y = len(matrix) - 1
    total_score = 0

    for y in range(max_y+1):
        for x in range(max_x+1):
            """
            M.S
            .A.
            M.S
            """
            try:
                if matrix[y][x] == "M" and matrix[y+1][x+1] == "A" and matrix[y+2][x+2] == "S" and \
                        matrix[y+2][x] == "M" and matrix[y+1][x+1] == "A" and matrix[y][x+2] == "S":
                    total_score += 1
            except IndexError:
                pass

            """
            S.M
            .A.
            S.M
            """
            try:
                if matrix[y][x] == "S" and matrix[y+1][x+1] == "A" and matrix[y+2][x+2] == "M" and \
                        matrix[y+2][x] == "S" and matrix[y+1][x+1] == "A" and matrix[y][x+2] == "M":
                    total_score += 1
            except IndexError:
                pass

            """
            S.S
            .A.
            M.M
            """
            try:
                if matrix[y][x] == "S" and matrix[y+1][x+1] == "A" and matrix[y+2][x+2] == "M" and \
                        matrix[y+2][x] == "M" and matrix[y+1][x+1] == "A" and matrix[y][x+2] == "S":
                    total_score += 1
            except IndexError:
                pass

            """
            M.M
            .A.
            S.S
            """
            try:
                if matrix[y][x] == "M" and matrix[y+1][x+1] == "A" and matrix[y+2][x+2] == "S" and \
                        matrix[y+2][x] == "S" and matrix[y+1][x+1] == "A" and matrix[y][x+2] == "M":
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
    main(False)