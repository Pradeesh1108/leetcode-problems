#plain DFS

def min_knight_moves_plain_dfs(n, start, target):
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    visited = set()

    def dfs(x, y, steps):
        if (x, y) == target:
            return steps

        visited.add((x, y))

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in visited:
                res = dfs(nx, ny, steps + 1)
                if res != -1:
                    return res

        return -1

    return dfs(start[0], start[1], 0)



#DFS with BT

def min_knight_moves_backtracking(n, start, target):
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    visited = set()
    ans = float('inf')

    def backtrack(x, y, steps):
        nonlocal ans

        if steps >= ans:
            return

        if (x, y) == target:
            ans = steps
            return

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in visited:
                visited.add((nx, ny))
                backtrack(nx, ny, steps + 1)
                visited.remove((nx, ny))  # undo

    visited.add(start)
    backtrack(start[0], start[1], 0)

    return ans if ans != float('inf') else -1


#DP, BFD + DP Table

from collections import deque

def min_knight_moves_dp(n, start, target):
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    queue = deque([start])
    dp[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        if (x, y) == target:
            return dp[x][y]

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and dp[nx][ny] == -1:
                dp[nx][ny] = dp[x][y] + 1
                queue.append((nx, ny))

    return -1

#Dijkstra's algo

import heapq

def min_knight_moves_dijkstra(n, start, target):
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dist[start[0]][start[1]] = 0

    heap = [(0, start[0], start[1])]

    while heap:
        cost, x, y = heapq.heappop(heap)

        if (x, y) == target:
            return cost

        if cost > dist[x][y]:
            continue

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n:
                new_cost = cost + 1
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return -1

#BFS

from collections import deque

def bfs_knight_moves(n, start, target):
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    queue = deque([(start[0], start[1], 0)])
    visited = set([start])

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == target:
            return steps

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return 0

#Greedy

import math

def knight_greedy(n, start, target):
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    visited = set()
    x, y = start
    steps = 0

    while (x, y) != target:
        visited.add((x, y))
        candidates = []

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in visited:
                dist = math.dist((nx, ny), target)
                candidates.append((dist, nx, ny))

        if not candidates:
            return -1

        candidates.sort()
        _, x, y = candidates[0]
        steps += 1

    return steps


N = 8
start = (1, 1)
end = (8, 8)

# print(min_knight_moves_plain_dfs(N, start,end))
# print(min_knight_moves_backtracking(N, start, end))
# print(min_knight_moves_dp(N, start, end))
# print(min_knight_moves_dijkstra(N, start, end))
# print(bfs_knight_moves(N, start, end))
# print(knight_greedy(N, start, end))
