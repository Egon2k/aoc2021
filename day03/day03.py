def part1(data):
    gamma = ""
    epsilon = ""
    l = len(data[0])
    h = len(data)


    for i in range(l):
        zeros = 0
        for line in data:
            if line[i] == "0":
                zeros += 1
        
        if zeros > h/2:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma,2) * int(epsilon,2)
            
def calc(data, rule):
    l = len(data[0])
    newData = data[::]
    
    for i in range(l):
        zeros = 0
        for line in newData:
            if line[i] == "0":
                zeros += 1
        
        if zeros > len(newData)/2:
            if rule == 0:
                newData = [j for j in newData if j[i] == '0']
            else:
                newData = [j for j in newData if j[i] == '1']
        else:
            if rule == 0:
                newData = [j for j in newData if j[i] == '1']
            else:
                newData = [j for j in newData if j[i] == '0']

        if len(newData) == 1:
            return int(newData[0], 2)

def part2(data):
    return calc(data,0) * calc(data,1)
            
if __name__ == "__main__":
    data = []

    with open('day03/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))