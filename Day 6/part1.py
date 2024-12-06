from time import sleep


def main(debug=False):
    with open("inputtest.txt" if debug else "input.txt", "r") as file:
        matrix = []

        for row in file.readlines():
            matrix.append(list(row.strip()))
    max_x, max_y = len(matrix[0]) - 1, len(matrix) - 1

    steps = 1
    player_pos = []

    for index, row in enumerate(matrix):
        if "^" in row:
            print(row.index("^"), index)
            player_pos = [row.index("^"), index] # X, Y

    while True:
        if matrix[player_pos[1]][player_pos[0]] == "^":
            if 0 > player_pos[1] - 1 or player_pos[1] - 1 > max_y:
                break
            elif matrix[player_pos[1] - 1][player_pos[0]] == "#":
                matrix[player_pos[1]][player_pos[0]] = ">"
            else:
                if matrix[player_pos[1] - 1][player_pos[0]] == ".":
                    steps += 1

                matrix[player_pos[1] - 1][player_pos[0]] = "^"
                matrix[player_pos[1]][player_pos[0]] = "X"
                player_pos = [player_pos[0], player_pos[1] - 1]


        elif matrix[player_pos[1]][player_pos[0]] == ">":
            if 0 > player_pos[0] + 1 or player_pos[0] + 1 > max_x:
                break
            elif matrix[player_pos[1]][player_pos[0] + 1] == "#":
                matrix[player_pos[1]][player_pos[0]] = "v"
            else:
                if matrix[player_pos[1]][player_pos[0] + 1] == ".":
                    steps += 1

                matrix[player_pos[1]][player_pos[0] + 1] = ">"
                matrix[player_pos[1]][player_pos[0]] = "X"
                player_pos = [player_pos[0] + 1, player_pos[1]]


        elif matrix[player_pos[1]][player_pos[0]] == "v":
            if 0 > player_pos[1] + 1 or player_pos[1] + 1 > max_y:
                break
            elif matrix[player_pos[1] + 1][player_pos[0]] == "#":
                matrix[player_pos[1]][player_pos[0]] = "<"
            else:
                if matrix[player_pos[1] + 1][player_pos[0]] == ".":
                    steps += 1

                matrix[player_pos[1]][player_pos[0]] = "X"
                matrix[player_pos[1] + 1][player_pos[0]] = "v"
                player_pos = [player_pos[0], player_pos[1] + 1]


        elif matrix[player_pos[1]][player_pos[0]] == "<":
            if 0 > player_pos[0] - 1 or player_pos[0] - 1 > max_x:
                break
            elif matrix[player_pos[1]][player_pos[0] - 1] == "#":
                matrix[player_pos[1]][player_pos[0]] = "^"
            else:
                if matrix[player_pos[1]][player_pos[0] - 1] == ".":
                    steps += 1

                matrix[player_pos[1]][player_pos[0]] = "X"
                matrix[player_pos[1]][player_pos[0] - 1] = "<"
                player_pos = [player_pos[0] - 1, player_pos[1]]

        for row in matrix:
            print("".join(row))
        sleep(0.01)

        print(steps, player_pos)



if __name__ == "__main__":
    main(debug=False)