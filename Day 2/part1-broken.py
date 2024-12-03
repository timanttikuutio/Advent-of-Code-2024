from itertools import count


def main():
    with open("input.txt", "r") as file:
        reports = file.readlines()

    safe_reports = 0

    for report in reports:
        levels = [int(i) for i in report.strip("\n").split(" ")]

        levels_diff = []
        levels_diff_two = []

        for index, level in enumerate(levels):
            if index != len(levels) - 1:
                if int(level) > levels[index + 1] and 1 <= (level - levels[index + 1]) <= 3:
                    levels_diff.append(True)
                else:
                    levels_diff.append(False)

                if int(level) < levels[index + 1] and 1 <= (levels[index + 1] - level) <= 3:
                    levels_diff_two.append(True)
                else:
                    levels_diff_two.append(False)

        if all(levels_diff) or all(levels_diff_two):
            safe_reports += 1

    print(safe_reports)

if __name__ == '__main__':
    main()