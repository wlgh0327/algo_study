# 구구단 곱셈표 출력하기

print('-' * 27)

for i in range(1, 10) :
    for j in range(1, 10) :
        print('{:3}'.format(i * j), end='')
    print()

print('-' * 27)
