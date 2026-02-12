def solution(x):
    ls=sum(map(int,str(x)))
    if x%ls==0:
        return True
    else:
        return False
