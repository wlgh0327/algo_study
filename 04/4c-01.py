""" Fixed stack with collections.deque """

from typing import Any
from collections import deque

class Stack :

    def __init__(self, maxlen: int = 256) -> None :
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int :
        return len(self.__stk)

    def is_empty(self) -> bool :
        return not self.__stk

    def is_full(self) -> bool :
        return len(self.__sk) == self.__stk.maxlen

    def push(self, value: Any) -> None :
        self.__stk.append(value)

    def pop(self) -> Any :
        return self.__stk.pop()

    def peek(self) -> Any :
        return self.__stk[-1]

    def clear(self) -> None :
        self.__stk.clear()

    def find(self, value: Any) -> Any :
        try :
            return self.__stk.index(value)
        except ValueError :
            return -1

    def count(self, value: Any) -> int :
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool :
        return self.count(value)

    def dump(self) -> int :
        print(list(self.__stk))


from enum import Enum


Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu :
    s = ['({}){}'.format(m.value, m.name) for m in Menu]
    while True :
        print(*s, sep='    ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)


s = Stack(64)


while True :
    print('Current # of data : {} / {}'.format(len(s), s.capacity))

    menu = select_menu()

    if menu == Menu.Push :
        x = int(input('Input a data : '))
        try :
            s.push(x)
        except :
            print('Stack is Full')


    elif menu == Menu.Pop :
        try :
            x = s.pop()
            print('{} popped'.format(x))
        except  :
            print('Stack is empty')

    elif menu == Menu.Peek :
        try :
            x = s.peek()
            print('Peeked data is {}'.format(x))
        except  :
            print('Stack is empty')

    elif menu == Menu.Search :
        x = int(input('Input a data to search : '))
        if x in s :
            print('{} contained, first position is {}'.format(s.count(x), s.find(x)))
        else :
            print("Can't find value")

    elif menu == Menu.Dump :
        s.dump()
    else :
        break

