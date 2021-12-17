ELEVEN_BITS = 11
FIFTEEN_BITS = 15
VERSION_LEN = 3
TARGET_LEN = 3
LITERAL_LEN = 4

def get_bits(bits, i, no):
    return int(bits[i: i+no], 2), i + no

def solve(bits, pos):
    v, pos = get_bits(bits, pos, VERSION_LEN)
    t, pos = get_bits(bits, pos, TARGET_LEN)

    version_total = v
    value = 0

    if t == 4:
        literals = []
        while True:
            sub_bits = int(bits[pos])
            pos = pos + 1 
            literal, pos = get_bits(bits, pos, LITERAL_LEN)
            literals.append(literal)

            if sub_bits == 0: 
                break
        vs = 0

        for literal in literals:
            vs = (vs * 16) + literal
        value = vs
    else:
        values = []
        i, pos = get_bits(bits, pos, 1)
        if i == 0: 
            l_length, pos = get_bits(bits, pos, FIFTEEN_BITS)
            start = pos
            while pos < start + l_length:
                version_sum, v, pos = solve(bits, pos)
                version_total += version_sum
                values.append(v)
        else: 
            l_number, pos = get_bits(bits, pos, ELEVEN_BITS)
            for _ in range(l_number):
                version_sum, v, pos = solve(bits, pos)
                version_total += version_sum
                values.append(v)
                
        if t == 0:
            value = sum(values)
        elif t == 1:
            value = 1
            for v in values:
                value *= v
        elif t == 2:
            value = min(values)
        elif t == 3:
            value = max(values)
        elif t == 5:
            if values[0] > values[1]:
                value = 1
            else:
                value = 0
        elif t == 6:
            if values[0] < values[1]:
                value = 1
            else:
                value = 0
        elif t == 7:
            if values[0] == values[1]:
                value = 1
            else:
                value = 0

    return version_total, value, pos

def part1(data):
    binary = bin(int(data,16))[2:]
    return solve(binary, 0)[0]

def part2(data):
    binary = bin(int(data,16))[2:]
    return solve(binary, 0)[1]

if __name__ == '__main__':
    data = []

    with open('day16/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data[0]))
    print(part2(data[0]))
