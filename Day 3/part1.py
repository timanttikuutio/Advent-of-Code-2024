import re

def main():
    with open("input.txt", "r") as file:
        data = file.read()

    end_result = 0

    results = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data)

    for result in results:
        splitre = re.findall(r"[0-9]{1,3}", result)
        end_result += int(splitre[0]) * int(splitre[1])

    print(end_result)

if __name__ == "__main__":
    main()

