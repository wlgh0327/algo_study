# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print('{}의 최댓값은 {}입니다.'.format(t, max_of(t)))
print('{}의 최댓값은 {}입니다.'.format(s, max_of(s)))
print('{}의 최댓값은 {}입니다.'.format(a, max_of(a)))

