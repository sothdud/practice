def solution(n, control):
    #딕셔너리 방식: 키 값을 미리 저장해놓음
    key={"w":+1,"s":-1, "d":+10, "a":-10}
    for c in control:
        #해당문자에 맞는 키값을받아서 더해줌
        n+=key[c]

    return n
