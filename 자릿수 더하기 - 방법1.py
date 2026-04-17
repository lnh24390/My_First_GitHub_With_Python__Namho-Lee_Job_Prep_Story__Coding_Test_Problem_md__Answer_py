
def solution(N):
    total = 0

    # N이 0보다 클 때까지 반복
    while N > 0:
        total += N % 10   # 마지막 자리 추출
        N //= 10          # 마지막 자리 제거

    return total
