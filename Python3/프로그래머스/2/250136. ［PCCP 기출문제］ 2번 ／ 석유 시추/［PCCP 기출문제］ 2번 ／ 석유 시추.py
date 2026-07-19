from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]

    # 각 열에 시추관을 설치했을 때 얻을 수 있는 석유량
    oil_by_column = [0] * m

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for row in range(n):
        for col in range(m):

            # 석유가 없거나 이미 방문한 위치는 건너뜀
            if land[row][col] == 0 or visited[row][col]:
                continue

            queue = deque([(row, col)])
            visited[row][col] = True

            oil_size = 0

            # 이 석유 덩어리가 걸쳐 있는 열
            columns = set()

            while queue:
                current_row, current_col = queue.popleft()

                oil_size += 1
                columns.add(current_col)

                for dr, dc in directions:
                    next_row = current_row + dr
                    next_col = current_col + dc

                    if not (0 <= next_row < n and 0 <= next_col < m):
                        continue

                    if land[next_row][next_col] == 0:
                        continue

                    if visited[next_row][next_col]:
                        continue

                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))

            # 현재 석유 덩어리가 걸쳐 있는 모든 열에
            # 덩어리 전체 크기를 더함
            for column in columns:
                oil_by_column[column] += oil_size

    return max(oil_by_column)