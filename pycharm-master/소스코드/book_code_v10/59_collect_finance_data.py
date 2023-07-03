import pandas_datareader as pdr
import datetime

# 1. 주가 데이터
start  =  datetime.datetime(2018, 1, 1)
end  =  datetime.datetime(2018, 12, 31)
df = pdr.get_data_yahoo("005930.KS", start, end)

# 2. 환율 데이터
start  =  datetime.datetime(2018, 1, 1)
end  =  datetime.datetime(2019, 4, 31)
df = pdr.get_data_fred("DCOILWTICO", start, end)

# 3. 원자재 가격 등
start  =  datetime.datetime(2018, 1, 1)
end  =  datetime.datetime(2019, 4, 31)
df = pdr.get_data_fred("DCOILWTICO", start, end)

