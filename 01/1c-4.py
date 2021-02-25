# 함수 내부 외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n = 1           # 전역 변수(함수 내부/외부에서 사용)
def put_id() :
    x = 1       # 지역 변수(함수 내부에서만 사용)
    print('id(x) = {}'.format(id(x)))


print('id(1) = {}'.format(id(1)))
print('id(n) = {}'.format(id(n)))

put_id()
