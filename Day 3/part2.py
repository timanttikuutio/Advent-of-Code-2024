import re

def main():
    with open("input.txt", "r") as file:
        data = file.read()

    end_result = 0
    addition_state = True

    results = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", data)

    for result in results:
        if result == "do()":
            addition_state = True
        elif result == "don't()":
            addition_state = False
        elif addition_state:
            splitre = re.findall(r"[0-9]{1,3}", result)
            end_result += int(splitre[0]) * int(splitre[1])

    print(end_result)

if __name__ == "__main__":
    main()
