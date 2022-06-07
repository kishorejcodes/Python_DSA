def hasPath(matrix, src, dest, visited):
    [a, b] = src
    if (src == dest):
        return True
    if ((a,b) in visited): return
    visited.add((a,b))
    for direction in matrix[a][b]:
        if (direction == "left"):
            m, n = 0, -1
        elif (direction == "right"):
            m, n = 0, 1
        elif (direction == "up"):
            m, n = -1, 0
        elif (direction == "down"):
            m, n = 1, 0
        cond = (a+m < 0 or a+m >= len(matrix))or(b+n < 0 or b+n >= len(matrix[0])) or (oppositeConnection(direction) not in  matrix[a+m][b+n])
        if (cond) :
            continue
        elif (hasPath(matrix, [a+m, b+n], dest,visited) == True):
                return True
    return False

def oppositeConnection(way):
    if (way == "left"): return "right"
    elif (way == "right"): return "left"
    elif (way == "up"): return "down"
    elif (way == "down"): return "up"

matrix = []
row1 = [ ["right", "down"],["left", "right"],["right"],["left","down"],["up","right"] ]
row2 = [ ["up", "right"],["left","right","down"],["left"],["up","down"],["up","down"] ]
row3 = [ ["right"],["left","right","up"],["right","down"],["left","right","up"],["left","right"] ]
row4 = [ ["left"],["up","right"],["left","up","down"],["right"],["left"] ]
row5 = [ ["left","down"],["left","right"],["left","right","up"],["left","right"],["down"] ]
matrix.extend([row1, row2, row3, row4, row5])

src = [4, 1]
dest = [0, 2]
visited = set()

print(hasPath(matrix, src, dest, visited))
