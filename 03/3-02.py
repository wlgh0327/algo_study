from seq_search import seq_search, seq_search_for, seq_search_for2, seq_search_for3
from typing import Any, Sequence

import time
import random

def bin_search(a: Sequence, key: Any) -> int :
    mid_idx = int(len(a)/2) - 1
    median_val = a[mid_idx]
    s = 0
    e = len(a) 
    if key > median_val :
        s = mid_idx
    else :
        e = mid_idx

    for i in range(s, e) :
        if key == a[i] :
            return i
    else :
        return -1

def bin_search2(a: Sequence, key: Any) -> int :

    s = 0
    e = len(a) - 1

    while True :
        m = (e + s) // 2
        #print('s : {}, m : {}, e : {}'.format(s, m, e))
        #print('a[s] : {}, a[m] : {}, a[e] : {}'.format(a[s], a[m], a[e]))
        if key == a[m] :
            return m
        elif a[m] < key :
            s = m + 1
        else :
            e = m - 1

        if s > e :
            break
        #input()
##

    return -1


        

if __name__ == '__main__' :
    
    num = int(input('원소 수를 입력하세요. : '))

    x = [None] * num

    for i in range(num) :
        x[i] = random.randint(1, num+1)

    ky = int(input('검색할 값을 입력하세요. : '))

    x.sort()
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

    start = time.time()
    idx = bin_search2(x, ky)
    end = time.time()
    bn_time = end - start

    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else :
        print('검색값은 x[{}]에 있습니다.'.format(idx))

    print('while문 시간(ms) : ', while_time * 1000)
    print('for문 시간(ms) : ', for_time * 1000)
    print('for2문 시간(ms) : ', for_time2 * 1000)
    print('for3문 시간(ms) : ', for_time3 * 1000)
    print('binary1 시간(ms) : ', bn_time * 1000)

