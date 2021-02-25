# 체인법으로 해시 함수 구현하기

#from __future__ import annotations
from typing import Any, Type
import hashlib

class Node :
    """ 해시를 구성하는 노드 """
    #def __init__(self, key: Any, value: Any, next: Node) -> None :
        #self.key = key
        #self.value = value
        #self.next = next

    def __init__(self, key, value, next) :
        self.key = key
        self.value = value
        self.next = next

class ChainedHash :
    """ 체인법으로 해시 클래스 구현"""

    def __init__(self, capacity : int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int :
        """ 해시값을 구함"""
        if isinstance(key, int) :
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any :
        """ 키가 key 인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None :
            if p.key == key :
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None :
            if p.key == key :
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True


    def remove(self, key: Any) -> bool :
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None :
            if p.key == key :
                if pp is None :
                    self.table[hash] = p.next
                else :
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity) :
            p = self.table[i]
            print(i, end='')
            while p is not None :
                print('    -> {} ({})'.format(p.key, p.value), end='')
                p = p.next
            print()




from enum import Enum

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu :
    s = ['({}){}'.format(m.value, m.name) for m in Menu]
    while True :
        print(*s, sep='    ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)


hash = ChainedHash(13)

while True :
    menu = select_menu()

    if menu == Menu.추가 :
        key = int(input('추가할 키를 입력하세요. : '))
        val = input('추가할 값을 입력하세요. : ')
        if not hash.add(key, val) :
            print('추가를 실패했습니다.')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요. : '))
        if not hash.remove(key) :
            print('삭제를 실패했습니다.')
    
    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력하세요. : '))
        t = hash.search(key)
        if t is not None :
            print('검색한 키를 갖는 값은 {}입니다.'.format(t))
        else :
            print('검색할 데이터가 없습니다.')
    elif menu == Menu.덤프 :
        hash.dump()

    else :
        break

