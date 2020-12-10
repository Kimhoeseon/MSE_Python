low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []  # 변동폭을 추가하기 위해 리스트 생성
for i in range(5) : #5일간의 변동폭이므로 5번 반복
    변동폭 = high_prices[i] - low_prices[i]
    volatility.append(변동폭)  #append()함수를 이용해서 변동폭이 반복될 때 리스트에 추가된다.
print(volatility)   