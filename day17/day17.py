'''
Gewalt ist auch eine Lösung!
'''

# puzzle data
# target area: x=111..161, y=-154..-101

X_LOWER = 111
X_UPPER = 161
Y_LOWER = -154
Y_UPPER = -101

def shoot(x_start, y_start):
    pos = list((0, 0))
    y_max = 0
    x = x_start
    y = y_start
    while (not(x > X_UPPER or y < Y_LOWER)):
        pos[0] += x
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        pos[1] += y
        y -= 1

        if pos[1] > y_max:
            y_max = pos[1]

        if X_LOWER <= pos[0] <= X_UPPER and Y_LOWER <= pos[1] <= Y_UPPER:
            return y_max, True
    
    return 0, False
        
def part12():
    y_hits = list()
    
    for x in range(X_UPPER + 4):
        for y in range(Y_LOWER - 1, 1000):
            y_max, hit = shoot(x, y)
            if hit:
                y_hits.append(y_max)
                print(max(y_hits), len(y_hits))
        
    return max(y_hits), len(y_hits)

if __name__ == '__main__':
    print(f'final = {part12()}')
