from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))
        print(x,y)

        if x == 2 or y == 2:
            print("Goal reached")
            return

        queue.append((4,y))
        queue.append((x,3))
        queue.append((0,y))
        queue.append((x,0))
        queue.append((x-min(x,3-y), y+min(x,3-y)))
        queue.append((x+min(y,4-x), y-min(y,4-x)))

water_jug()