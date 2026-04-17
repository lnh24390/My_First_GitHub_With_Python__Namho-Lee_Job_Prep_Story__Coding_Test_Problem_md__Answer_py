def solution(arr):
    arr.sort()
    
    # 정렬 후 1부터 n까지인지 확인
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return False
    return True
