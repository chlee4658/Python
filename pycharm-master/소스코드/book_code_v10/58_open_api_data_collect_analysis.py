# coding=utf-8

import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

import json

if __name__ == "__main__":
    key ="오픈API키를 입력합니다."

    # 1. 데이터 수집하기
    # https://ecos.bok.or.kr/jsp/openapi/OpenApiController.jsp?t=guideServiceDtl&apiCode=OA-1040&menuGroup=MENU000004
    # 여기서 주소 만들면 쉽다.

    url="http://ecos.bok.or.kr/api/StatisticSearch/"+key+"/json/kr/1/1000/085Y026/MM/201501/201905/I16A/?/?/"
    result = urllib.request.urlopen(url)
    json_return = result.read()

    dict_return = json.loads(json_return)
    dict_return = dict_return["StatisticSearch"]["row"]

    eco = pd.DataFrame(dict_return)
    eco.groupby("ITEM_CODE1").count()
    eco.dtypes

    eco["DATA_VALUE"] = eco["DATA_VALUE"].astype(float)

    # 2. 날짜와 시간으로 바꾸기
    # prd["TIME"] = prd["TIME"].astype(str)
    eco["DATE"] = eco["TIME"].str[0:4] + "-" + eco["TIME"].str[4:6] + "-" + "01"
    eco['DATE'] = eco['DATE'].astype('datetime64[ns]')


    import seaborn as sns

    sns.set(style="darkgrid")
    sns.lineplot(x="DATE", y="DATA_VALUE", hue="ITEM_CODE1", data=eco)

    # 3. 주가데이터 수집하기
    url = "http://ecos.bok.or.kr/api/StatisticSearch/" + key + "/json/kr/1/1000/028Y015/MM/198001/201905/1080000/?/?"
    result = urllib.request.urlopen(url)
    json_return = result.read()

    dict_return = json.loads(json_return)
    dict_return = dict_return["StatisticSearch"]["row"]
    stock = pd.DataFrame(dict_return)

    stock["DATA_VALUE"] = stock["DATA_VALUE"].astype(float)
    stock["DATE"] = stock["TIME"].str[0:4] + "-" + stock["TIME"].str[4:6] + "-" + "01"
    stock['DATE'] = stock['DATE'].astype('datetime64[ns]')

    sns.lineplot(x="DATE", y="DATA_VALUE", data=stock)

    import datetime

    # 4. 경기선행지수와 KOSPI지수 비교하기
    stock_df = stock[["DATE", "DATA_VALUE"]]
    stock_df = stock_df.rename(columns={"DATA_VALUE":"STOCK"})
    stock_df = stock_df[stock_df["DATE"] >= datetime.datetime(2015, 1, 1)]

    df = pd.merge( stock_df, eco[["DATE", "DATA_VALUE"]], on="DATE", how="left")

    sns.lineplot(x="DATE", y="STOCK", data=df)
    sns.lineplot(x="DATE", y="DATA_VALUE", data=df)

    df["STOCK_NEW"] = ( df["STOCK"] - df["STOCK"].min() ) / ( df["STOCK"].max() - df["STOCK"].min() )
    df["ECO_NEW"] = (df["DATA_VALUE"] - df["DATA_VALUE"].min()) / ( df["DATA_VALUE"].max() - df["DATA_VALUE"].min() )

    plt.figure()
    sns.lineplot(x="DATE", y="STOCK_NEW", data=df)
    sns.lineplot(x="DATE", y="ECO_NEW", data=df)
    plt.draw()

    df["dif"] = df["STOCK_NEW"] - df["ECO_NEW"]
    df["dif"] = df["dif"].abs()
    dif_sum = df["dif"].sum()
    print("0개월 간의 차이합은 {}입니다.".format(dif_sum))

    # 5. 경기선행지수와 KOSPI지수 산점도 비교하기
    plt.figure()
    sns.scatterplot(x="ECO_NEW", y="STOCK_NEW", data=df)
    plt.show()

    # 6. 경기선행지수와 KOSPI지수 산점도 비교하기
    df_bef_5= df[df["DATE"]<="2018-05-01"]

    df_bef_5["STOCK_NEW"] = ( df_bef_5["STOCK"] - df_bef_5["STOCK"].min() ) / ( df_bef_5["STOCK"].max() - df_bef_5["STOCK"].min() )
    df_bef_5["ECO_NEW"] = (df_bef_5["DATA_VALUE"] - df_bef_5["DATA_VALUE"].min()) / ( df_bef_5["DATA_VALUE"].max() - df_bef_5["DATA_VALUE"].min() )

    plt.figure()
    sns.scatterplot(x="ECO_NEW", y="STOCK_NEW", data=df_bef_5)
    plt.show()

    # 7. 1개월 뒤의 코스피지수와 비교
    m = 1
    stock_temp = df_bef_5.copy()
    stock_temp["DATE"] = stock_temp["DATE"] + pd.DateOffset(months=m)

    stock_temp = pd.merge(stock_temp.drop("DATA_VALUE", 1), eco[["DATE", "DATA_VALUE"]], on="DATE", how="left")
    stock_temp = stock_temp.dropna()

    stock_temp["STOCK_NEW"] = (stock_temp["STOCK"] - stock_temp["STOCK"].min()) / (stock_temp["STOCK"].max() - stock_temp["STOCK"].min())
    stock_temp["ECO_NEW"] = (stock_temp["DATA_VALUE"] - stock_temp["DATA_VALUE"].min()) / (stock_temp["DATA_VALUE"].max() - stock_temp["DATA_VALUE"].min())

    plt.figure()
    sns.scatterplot(x="ECO_NEW", y="STOCK_NEW", data=stock_temp)
    plt.draw()

    cor = stock_temp[["STOCK_NEW", "ECO_NEW"]].corr()
    print("{}개월 간의 상관계수는 {}입니다.".format(m, cor["ECO_NEW"][0]))

    import time

    # 8. -3개월 4개월까지 상관계수 구해보기
    def index_dif(stock_df, m):
        stock_temp = stock_df.copy()
        stock_temp["DATE"] = stock_temp["DATE"] + pd.DateOffset(months=m)
        stock_temp = pd.merge(stock_temp.drop("DATA_VALUE", 1), eco[["DATE", "DATA_VALUE"]], on="DATE", how="left")
        stock_temp = stock_temp.dropna()

        stock_temp["STOCK_NEW"] = (stock_temp["STOCK"] - stock_temp["STOCK"].min()) / (stock_temp["STOCK"].max() - stock_temp["STOCK"].min())
        stock_temp["ECO_NEW"] = (stock_temp["DATA_VALUE"] - stock_temp["DATA_VALUE"].min()) / (stock_temp["DATA_VALUE"].max() - stock_temp["DATA_VALUE"].min())

        plt.figure()
        sns.scatterplot(x="ECO_NEW", y="STOCK_NEW", data=stock_temp)
        plt.draw()

        cor = stock_temp[["STOCK_NEW", "ECO_NEW"]].corr()
        print("{}개월 간의 상관계수는 {}입니다.".format(m, cor["ECO_NEW"][0]))

    for m in range(-3,4):
        index_dif(df_bef_5, m)
