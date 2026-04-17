def solution(sticker):
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    # 선형 DP 함수
    def rob(arr):
        prev2, prev1 = 0, 0
        for num in arr:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1
    
    # 두 경우 비교
    return max(
        rob(sticker[:-1]),  # 마지막 제외
        rob(sticker[1:])    # 첫 번째 제외
    )
