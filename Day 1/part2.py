from itertools import count


def main():
    with open("input.txt", "r") as file:
        inputdata = file.readlines()

    leftl, rightl = [], []
    score = 0

    for i in inputdata:
        leftl.append(i.split()[0])
        rightl.append(i.split()[1])

    for j in leftl:
        if j in rightl:
            score += int(int(j) *  rightl.count(j))

    print(score)

if __name__ == '__main__':
    main()