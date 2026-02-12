def solution(n):
    ls = sorted(str(n),reverse=True) # 결과는 리스트로 나옴 reverse 해야 내림차순으로됨
    s="".join(ls)
    
    return int(s)