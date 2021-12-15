'''
Räder sind nicht dafür da, sie neu zu erfinden.
'''
import heapq, sys

DIR = [(1,0), (-1,0), (0,1), (0,-1)]

# https://stackoverflow.com/a/58833232
def dijkstra(g, s, t):
    q = []
    d = {k: sys.maxsize for k in g.keys()}
    p = {}

    d[s] = 0 
    heapq.heappush(q, (0, s))

    while q:
        last_w, curr_v = heapq.heappop(q)
        for n, n_w in g[curr_v]:
            cand_w = last_w + n_w # equivalent to d[curr_v] + n_w 
            #print(d) # uncomment to see how deltas are updated
            if cand_w < d[n]:
                d[n] = cand_w
                p[n] = curr_v
                heapq.heappush(q, (cand_w, n))

    #print("predecessors: ", p )
    #print("delta: ", d )
    return d[t]

def part1(grid, dest):
    return dijkstra(grid, (0,0), dest)
    
def part2(data):
    pass

def process_data(data):
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

if __name__ == '__main__':
    data = []

    with open('day15/data.txt') as f:
        for line in f:
            data.append([int(x) for x in line.strip()])

    grid = process_data(data)

    print(part1(grid, (len(data) - 1,len(data) - 1)))
    print(part2(data))