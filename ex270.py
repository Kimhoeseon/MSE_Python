# 종목의 리스트 생성
종목 = [] 

# 삼성,현대,Lg 리스트를 만든다.
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

#종목 리스트에 삼성,현대,lg를 넣는다.
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)   

# i는 삼성,현대,Lg순으로 반복하여 code와 per 출력