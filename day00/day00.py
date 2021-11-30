if __name__ == "__main__":
    data = []

    with open('data.txt') as f:
        for line in f:
            data.append(line.strip())
