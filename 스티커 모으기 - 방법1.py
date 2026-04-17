def solution(sticker):
    n = len(sticker)
    
    # 예외 처리
    if n == 1:
        return sticker[0]
    
    # Case 1: 첫 번째 포함 → 마지막 제외
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    
    for i in range(2, n-1):  # 마지막 제외
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    # Case 2: 첫 번째 제외 → 마지막 포함 가능
    dp2 = [0] * n
    dp2[1] = sticker[1]
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    return max(dp1[n-2], dp2[n-1])
