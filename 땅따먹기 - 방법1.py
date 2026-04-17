def solution(land):
    # 1행부터 마지막 행까지 진행
    for i in range(1, len(land)):
        for j in range(4):
            # 현재 열을 제외한 이전 행의 최대값
            land[i][j] += max(
                land[i-1][k] for k in range(4) if k != j
            )
    
    # 마지막 행에서 최대값 반환
    return max(land[-1])
