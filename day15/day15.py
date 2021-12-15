'''
Räder sind nicht dafür da, sie neu zu erfinden.
'''
import heapq, sys

DIR = [(1,0), (-1,0), (0,1), (0,-1)]

def dijkstra(g, s, t):
    '''
    https://stackoverflow.com/a/58833232
    '''
    q = []
    d = {k: sys.maxsize for k in g.keys()}
    p = {}

    d[s] = 0 
    heapq.heappush(q, (0, s))

    while q:
        last_w, curr_v = heapq.heappop(q)
        for n, n_w in g[curr_v]:
            cand_w = last_w + n_w # equivalent to d[curr_v] + n_w 
            if cand_w < d[n]:
                d[n] = cand_w
                p[n] = curr_v
                heapq.heappush(q, (cand_w, n))

    return d[t]

def solve(grid, dest):
    return dijkstra(grid, (0,0), dest)

def create_grid(data):
    '''
    creates grid from data
    '''
    grid = dict()

    for row in range(len(data[0])):
        for col in range(len(data)):
            weights = []
            for dir in DIR:
                node = (row + dir[0], col + dir[1])
                if 0 <= node[0] <= len(data) - 1 and \
                   0 <= node[1] <= len(data) - 1:
                    weight = data[row + dir[0]][col + dir[1]]
                    weights.append([node, weight])
                
            grid[(row,col)] = weights
    return grid

def extend_data(data):
    '''
    preparing data for part 2
    '''
    rows = len(data[0]) * 5
    cols = len(data) * 5
    new_data = [[0] * rows for i in range(cols)]
    for r in range(5):
        for c in range(5):
            for row in range(len(data[0])):
                for col in range(len(data)):
                    new_val = data[row][col] + r + c
                    if new_val > 9:
                        new_data[row + len(data[0]) * r][col + len(data) * c] = new_val % 9
                    else:
                        new_data[row + len(data[0]) * r][col + len(data) * c] = new_val
    return new_data

def part1(data):
    grid = create_grid(data)
    dest = (len(data) - 1,len(data) - 1)
    return solve(grid, dest)
    
def part2(data):
    data = extend_data(data)
    grid = create_grid(data)
    dest = (len(data) - 1,len(data) - 1)
    return solve(grid, dest)

if __name__ == '__main__':
    data = []

    with open('day15/data.txt') as f:
        for line in f:
            data.append([int(x) for x in line.strip()])

    print(part1(data))
    print(part2(data))