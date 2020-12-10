import requests       # requests()함수를 이용하여 htpp://ap~~ 에서 딕셔너리를 가져온다.
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

a = float(btc['opening_price'])   #시가   딕셔너리 안에 있는 opening_price를 가져온다.             
b = float(btc['max_price'])       #최고가 딕셔너리 안에 있는 max_price를 가져온다. 
c = float(btc['min_price'])       #최저가 딕셔너리 안에 있는 min_price를 가져온다.
d = b-c                           #변동폭 최고가인 b와 최저가인 c를 뺀다. 

if (a+d) > b:         
    print("상승장")   #시가+변동폭이 최고가보다 높을경우 출력된다.
else:
    print("하락장")   #시가+변동폭이 최고가보다 낮을경우 출력된다.