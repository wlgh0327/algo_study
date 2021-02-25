# while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

import time
import random


def seq_search(a: Sequence, key: Any) -> int :
    """ 시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while문)"""
    i = 0

    while True :
        if i == len(a) :
            return -1
        if a[i] == key :
            return i
        i += 1


# for 문으로 작성한 선형 검색 알고리즘
def num_generator(stop) :
    n = 0
    while n < stop :
        yield n
        n += 1

def seq_search_for(a: Sequence, key: Any) -> int :
    for i in range(len(a)) :
        if a[i] == key :
            return i

    return -1

def seq_search_for2(a: Sequence, key: Any) -> int :
    for i in num_generator(len(a)) :
        if a[i] == key :
            return i

    return -1

def seq_search_for3(a: Sequence, key: Any) -> int :
    count = 0
    for dat in a :
        if dat == key :
            return count
        count += 1

    return -1



if __name__ == '__main__' :
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num

    for i in range(num) :
        x[i] = int(input('x[{}] : '.format(i)))

    ky = int(input('검색할 값을 입력하세요. : '))

    idx = seq_search(x, ky)

    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')

    else :
        print('검색값은 x[{}]에 있습니다.'.format(idx))


    
    num = int(input('원소 수를 입력하세요. : '))

    x = [None] * num

    for i in range(num) :
        x[i] = random.randint(1, num+1)

    ky = int(input('검색할 값을 입력하세요. : '))

    start = time.time()
    idx = seq_search(x, ky)
    end = time.time()

    while_time = end - start

    start = time.time()
    idx = seq_search_for(x, ky)
    end = time.time()

    for_time = end - start

    start = time.time()
    idx = seq_search_for2(x, ky)
    end = time.time()

    for_time2 = end - start

    start = time.time()
    idx = seq_search_for3(x, ky)
    end = time.time()

    for_time3 = end - start


    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else :
        print('검색값은 x[{}]에 있습니다.'.format(idx))

    print('while문 시간(ms) : ', while_time * 1000)
    print('for문 시간(ms) : ', for_time * 1000)
    print('for2문 시간(ms) : ', for_time2 * 1000)
    print('for3문 시간(ms) : ', for_time3 * 1000)

