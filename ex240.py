def 함수0(num) :  
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :  
    num = num + 10
    return 함수1(num)

c = 함수2(2)      # 1.함수2(num)에 2를 대입하여 12가 된다. 2.return으로 함수1(num)에 12를 대입하여 14가 된다.
print(c)          # 3.return으로 함수0(num)으로 14가 대입하여 28이 출력된다.
