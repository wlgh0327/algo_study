# 가로, 세로 길이가 정수이고 넓이가 area인 직사강형에서 변의 길이 나열하기
# 약수 구하기
area = int(input('직사각형의 넓이를 입력하세요.: '))

ans = []

for i in range(1, area + 1) :
    if i * i > area :
        break
    if area % i :
        continue
    print('{} x {}'.format(i, area // i))
    ans.append(i)
    ans.append(area // i)

ans.sort()
print(ans)

