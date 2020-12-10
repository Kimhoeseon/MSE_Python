def message1():   # message1() 은 print("A")로 정의된다.
    print("A")

def message2():   # message2() 은 print("B")로 정의된다.
    print("B")

def message3():   # message3() 은 for문과 message1()로 정의된다.
    for i in range (3) :  # for문을 3번 반복
        message2()        # for문을 반복할 때 message2()로 B가 출력되며 그다음으로 C가 출력되는 것을 3번 반복한다.
        print("C")        
    message1()           # for문이 끝난 뒤 message1()으로 "A"가 출력된다.

message3()              # message3()출력