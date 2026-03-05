from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def bfs():
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        m, c, b = state

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for dm, dc in moves:
            if b == 1:
                new = (m-dm, c-dc, 0)
            else:
                new = (m+dm, c+dc, 1)

            if is_valid(new[0], new[1]):
                queue.append((new, path+[state]))

print(bfs())