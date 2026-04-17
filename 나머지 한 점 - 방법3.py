def solution(v):
    x_set = set()
    y_set = set()
    
    for x, y in v:
        # 있으면 제거, 없으면 추가
        if x in x_set:
            x_set.remove(x)
        else:
            x_set.add(x)
        
        if y in y_set:
            y_set.remove(y)
        else:
            y_set.add(y)
    
    return [x_set.pop(), y_set.pop()]
