ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
total_profit = 0    #처음의 총 수입은 0이다.
for row in ohlc[1:]:  # ["open"~"close"]를 제외한 나머지를 반복한다.
    profit = (row[3] - row[0]) # 리스트에서 1부터 3까지 중 종가인 row[3]에서 시가인 row[0]을 빼면 수입이 나온다.
    total_profit += profit     # 시작 수입이 0에서 얻은 수입들을 반복하면서 더해간다.
print(total_profit)            # 반복이 끝나 얻어진 총 수입을 출력한다.