x = ['John', 'George', 'Paul', 'Ringo']

# 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)
for i in range(len(x)) :
    print('x[{}] = {}'.format(i, x[i]))

# 리스트의 모든 원소를 enumerate() 함수로 스캔하기
for i, name in enumerate(x) :
    print('x[{}] = {}'.format(i, name))

# 리스트의 모든 원소를 enumerate() 함수로 스캔하기(1부터 카운트)
for i, name in enumerate(x, 1) :
    print('x[{}] = {}'.format(i, name))

# 리스트의 모든 원소를 스캔하기(인덱스 값을 사용하지 않음)
for i in x :
    print(i)




x = ('John', 'George', 'Paul', 'Ringo')

# 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)
for i in range(len(x)) :
    print('x[{}] = {}'.format(i, x[i]))

# 리스트의 모든 원소를 enumerate() 함수로 스캔하기
for i, name in enumerate(x) :
    print('x[{}] = {}'.format(i, name))

# 리스트의 모든 원소를 enumerate() 함수로 스캔하기(1부터 카운트)
for i, name in enumerate(x, 1) :
    print('x[{}] = {}'.format(i, name))

# 리스트의 모든 원소를 스캔하기(인덱스 값을 사용하지 않음)
for i in x :
    print(i)

