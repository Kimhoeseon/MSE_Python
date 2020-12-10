per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:                #""에서 예외가 발생하여 실행되므로 0이 출력
        print(0)
    else:
        print("clean data") # 에러가 없을 때 "clean data"가 출력
    finally:
        print("변환 완료")  # try,excepy,else 실행될때 출력