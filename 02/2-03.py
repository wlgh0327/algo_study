# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

from max import max_of

print('배열의 최댓값을 구합니다.')
print('주의 : "End"를 입력하면 종료합니다.')

number = 0
x = []                  # 빈 리스트

while True :
    s = input('x[{}]값을 입력하세요. : '.format(number))
    if s == 'End' :
        break
    x.append(int(s))
    number += 1

print('{}개를 입력했습니다.'.format(number))
print('최댓값은 {}입니다.'.format(max_of(x)))

