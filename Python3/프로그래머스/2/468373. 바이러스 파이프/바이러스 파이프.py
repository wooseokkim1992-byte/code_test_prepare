from functools import lru_cache


def solution(n, infection, edges, k):
    # 타입별 인접 리스트
    graph = [[[] for _ in range(n)] for _ in range(3)]

    for x, y, pipe_type in edges:
        x -= 1
        y -= 1
        pipe_type -= 1

        graph[pipe_type][x].append(y)
        graph[pipe_type][y].append(x)

    # 각 파이프 타입별 연결 요소를 비트마스크로 저장
    components = [[] for _ in range(3)]

    for pipe_type in range(3):
        visited = [False] * n

        for start in range(n):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True
            component_mask = 0

            while stack:
                current = stack.pop()
                component_mask |= 1 << current

                for next_node in graph[pipe_type][current]:
                    if not visited[next_node]:
                        visited[next_node] = True
                        stack.append(next_node)

            components[pipe_type].append(component_mask)

    def open_pipe(infected_mask, pipe_type):
        """
        pipe_type에 해당하는 파이프를 열었을 때
        새롭게 감염되는 노드를 계산한다.
        """
        next_mask = infected_mask

        for component_mask in components[pipe_type]:
            # 연결 요소 안에 감염된 노드가 하나라도 있다면
            if component_mask & infected_mask:
                # 연결 요소 전체가 감염된다.
                next_mask |= component_mask

        return next_mask

    @lru_cache(None)
    def dfs(infected_mask, remaining):
        # 행동을 더 하지 않고 끝내는 경우
        answer = infected_mask.bit_count()

        if remaining == 0:
            return answer

        # A, B, C 파이프를 각각 여는 경우
        for pipe_type in range(3):
            next_mask = open_pipe(infected_mask, pipe_type)

            answer = max(
                answer,
                dfs(next_mask, remaining - 1)
            )

        return answer

    initial_mask = 1 << (infection - 1)

    return dfs(initial_mask, k)