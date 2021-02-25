from enum import Enum
from fixed_stack import FixedStack


Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu :
    s = ['({}){}'.format(m.value, m.name) for m in Menu]
    while True :
        print(*s, sep='    ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)


s = FixedStack(64)

while True :
    print('Current # of data : {} / {}'.format(len(s), s.capacity))

    menu = select_menu()

    if menu == Menu.Push :
        x = int(input('Input a data : '))
        try :
            s.push(x)
        except FixedStack.Full :
            print('Stack is Full')


    elif menu == Menu.Pop :
        try :
            x = s.pop()
            print('{} popped'.format(x))
        except FixedStack.Empty :
            print('Stack is empty')

    elif menu == Menu.Peek :
        try :
            x = s.peek()
            print('Peeked data is {}'.format(x))
        except FixedStack.Empty :
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

