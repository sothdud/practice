

def solution(n,k):
    service=n//10
    
    k-=service
    answer=(12000*n)+(2000*k)
    
    return answer

#def solution(n, k):
 #   answer = 0
 #   if n%10==0:
  #      i=int(n/10)
   #     k-=i
    #    answer= (12000*n+2000*k)
   # else:
    #    i=int(n/10)
     #   k-=i
      #  answer=(12000*n+2000*k)
  #  return answer