

def main():
    with open("input.txt", "r") as file:
        inputdata = file.readlines()

    leftl, rightl = [], []
    totals = []

    for i in inputdata:
        leftl.append(i.split()[0])
        rightl.append(i.split()[1])

    leftl = sorted(leftl)
    rightl = sorted(rightl)

    for j in range(len(inputdata)):
        if leftl[j] >= rightl[j]:
            totals.append(int(leftl[j]) - int(rightl[j]))
        elif leftl[j] <= rightl[j]:
            totals.append(int(rightl[j]) - int(leftl[j]))

    print(sum(totals))

if __name__ == '__main__':
    main()