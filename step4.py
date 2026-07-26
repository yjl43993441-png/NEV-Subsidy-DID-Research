import pandas as pd
import os


# 数据路径
path = "stock_data"


# 股票文件和企业类型
stocks = {

    "比亚迪_sina_2018_2026.xlsx": 1,
    "北汽蓝谷_sina.xlsx": 1,
    "广汽集团_sina.xlsx": 1,
    "江淮汽车_sina.xlsx": 1,

    "上汽集团_sina.xlsx": 0,
    "长安汽车_sina.xlsx": 0,
    "一汽解放_sina.xlsx": 0,
    "福田汽车_sina.xlsx": 0,
    "金龙汽车_sina.xlsx": 0
}


all_data = []


for file, nev in stocks.items():

    print("正在处理：", file)

    filepath = os.path.join(path, file)

    df = pd.read_excel(filepath)


    # 统一日期格式
    df["date"] = pd.to_datetime(df["date"])


    # 按日期排序
    df = df.sort_values("date")


    # 计算股票收益率
    df["Return"] = (
        df["close"] - df["close"].shift(1)
    ) / df["close"].shift(1)


    # 删除第一行空收益率
    df = df.dropna()


    # 企业名称
    df["company"] = (
        file
        .replace("_sina.xlsx", "")
        .replace("_2018_2026", "")
    )


    # 新能源变量
    df["NEV"] = nev


    # 政策变量
    # 2023年以后补贴退出
    df["Policy"] = (
        df["date"].dt.year >= 2023
    ).astype(int)


    # DID交互项
    df["DID"] = (
        df["NEV"] *
        df["Policy"]
    )


    all_data.append(df)



# 合并
final = pd.concat(
    all_data,
    ignore_index=True
)


# 保存
final.to_excel(
    "DID_stock_data.xlsx",
    index=False
)


print("===================")
print("数据处理完成")
print("总样本量：",len(final))
print(final.head())
print("===================")