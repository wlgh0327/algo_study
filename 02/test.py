def convert(num, d) :
    
    arr = []

    template = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True :
        a = num % d
        num = num // d

        arr.append(template[a])
        if num == 0 :
            break

    arr.reverse()

    i = 0
    ret = ''
    while i < len(arr) :
        ret = ret + arr[i]
        i = i + 1

    return ret 

if __name__ == '__main__' :
    n = int(input('Input a decimal number : '))

    d = int(input('Input : '))
    print('{} -> {}'.format(n, convert(n, d)))
