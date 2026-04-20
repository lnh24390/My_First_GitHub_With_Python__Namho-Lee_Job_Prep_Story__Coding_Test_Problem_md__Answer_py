def solution(info, edges):
    from collections import defaultdict

    # 트리 구성
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)

    max_sheep = 0

    def dfs(sheep, wolf, possible_nodes):
        nonlocal max_sheep

        max_sheep = max(max_sheep, sheep)

        for i, node in enumerate(possible_nodes):
            next_sheep = sheep
            next_wolf = wolf

            # 현재 노드 방문
            if info[node] == 0:
                next_sheep += 1
            else:
                next_wolf += 1

            # 조건 위반 시 종료
            if next_wolf >= next_sheep:
                continue

            # 다음 후보 리스트 구성
            next_nodes = possible_nodes[:i] + possible_nodes[i+1:]
            next_nodes.extend(tree[node])

            dfs(next_sheep, next_wolf, next_nodes)

    # 시작: 루트(0)에서 시작
    dfs(1, 0, tree[0])

    return max_sheep
