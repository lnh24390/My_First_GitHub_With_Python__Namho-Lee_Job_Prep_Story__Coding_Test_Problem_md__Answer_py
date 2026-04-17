def solution(N):
    # 정수를 문자열로 변환 후 각 자리 숫자를 정수로 바꿔 합산
    return sum(int(digit) for digit in str(N))
