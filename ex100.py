date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))    # zip()함수를 사용하여 date을 key,close_price 을 value 로 묶는다.
print(close_table)  # zip함수를 이용한 리스트 출력