def main(debug=False):
    with open("inputtest.txt" if debug else "input.txt", "r") as file:
        data: list = file.read().splitlines()

    rules, pages = data[:data.index("")], data[data.index("")+1:]
    valid_pages = []
    page_sum = 0

    for page in pages:
        page = page.split(",")
        valid = True
        for rule in rules:
            left,right = rule.split("|")

            if left in page and right in page:
                if page.index(left) > page.index(right):
                    valid = False
        if valid:
            valid_pages.append(page)

    for i in valid_pages:
        length = len(i)

        page_sum += int(i[int(length-length/2)])

    print(page_sum)


if __name__ == "__main__":
    main(True)