import pandas as pd


# 读取step4生成的数据
df = pd.read_excel(
    "DID_stock_data.xlsx"
)


print("数据读取成功")
print(df.head())


# 描述性统计

variables = [
    "Return",
    "NEV",
    "Policy",
    "DID"
]


desc = df[variables].describe().T


# 保留需要的指标

result = desc[
    [
        "count",
        "mean",
        "std",
        "min",
        "max"
    ]
]


print("================")
print(result)


# 保存Excel

result.to_excel(
    "stock_data/描述性统计结果.xlsx"
)


print("保存成功")