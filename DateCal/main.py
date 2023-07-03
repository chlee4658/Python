from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



import re

def after_day(bdate, interval):
    oneday = bdate + timedelta(days = int(interval))
    print("그 날짜는 {0!s} 입니다.".format(oneday.strftime('%Y-%m-%d')))

def after_month(bdate, interval):
    oneday = bdate + relativedelta(months = int(interval))
    print("{0} 보다 {1}개월 뒤의 날짜는 {2!s} 입니다.".format(bdate, int(interval), oneday.strftime('%Y-%m-%d')))


print("계산하기 원하는 날짜를 2000-01-01 형태로 입력해 주세요  ")
anydate = input()
base_date = datetime.strptime(anydate, format('%Y-%m-%d')).date()

print("언제 날짜를 알고 싶으십니까? (입력 스타일: 5일, 10주, 3개월) ")
int_date = input()

if int_date[-1] == "일":
    idate = re.findall("\d+", int_date)
    after_day(base_date, idate[0])

if int_date[-2:] == "개월":
    idate = re.findall("\d+", int_date)
    after_month(base_date, idate[0])

# print("몇일 후 날짜를 원하시나요? ")
# inp = int(input())

#
# inp = 5
#
# oneday = today + timedelta(days =+ int(inp))
# print("그 날짜는 {0!s} 입니다.".format(oneday.strftime('%Y-%m-%d')))
#
# # 4주 후의 날짜
#
# after_wks = 4
# oneday = today + timedelta(days =+ after_wks * 7)
# print("그 날짜는 {0!s} 입니다.".format(oneday.strftime('%Y-%m-%d')))
#
# # 5개월 후의 날짜
# after_month = 5
# oneday = today + relativedelta(months =+ after_month)
# print("그 날짜는 {0!s} 입니다.".format(oneday.strftime('%Y-%m-%d')))