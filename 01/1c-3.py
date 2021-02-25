# 2자리 양수(10~99) 입력받기

print('2자리 양수를 입력하세요.')

def first() :
    while True:
        no = int(input('값을 입력하세요.: '))
        if no >= 10 and no <= 99 :
            break

    print('입력받은 양수는 {}입니다.'.format(no))


def second() :
    while True :
        no = int(input('값을 입력하세요.: '))
        if not(no < 10 or no > 99) :
            break

if __name__ == '__main__' :
    first()

    second()
