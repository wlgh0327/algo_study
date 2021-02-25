# 1,000 이하의 소수를 나열하기 (알고리즘 개선 1)

counter = 0
ptr = 0
prime = [None] * 500


prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2) : 
    for i in range(1, ptr) :
        counter += 1
        if n % prime[i] == 0 : # 나누어 떨어지면 소수가 아님
            break

    else :
        prime[ptr] = n  # 소수로 배열에 등록
        ptr += 1

for i in range(ptr) :
    print(prime[i])

print('나눗셈을 실행한 횟수 : {}'.format(counter))
