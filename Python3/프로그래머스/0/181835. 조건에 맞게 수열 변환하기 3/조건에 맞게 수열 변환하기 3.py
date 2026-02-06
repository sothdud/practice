def solution(arr, k):
    # k가 홀수인지 짝수인지 먼저 확인
    if k % 2 == 1:  # 홀수라면
        for i in range(len(arr)):
            arr[i] = arr[i] * k  # i번째 값을 k배로 수정
    else:           # 짝수라면
        for i in range(len(arr)):
            arr[i] = arr[i] + k  # i번째 값에 k를 더함
            
    return arr