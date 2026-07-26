import pandas as pd

from linearmodels.panel import PanelOLS


# ==========================
# 1.读取数据
# ==========================

df = pd.read_excel(
    "DID_stock_data.xlsx"
)


print("数据读取成功")


# ==========================
# 2.构造面板数据索引
# ==========================

# 日期转时间格式

df["date"] = pd.to_datetime(df["date"])


# 企业名称作为个体
# 日期作为时间

df = df.set_index(
    ["company", "date"]
)


print(df.head())


# ==========================
# 3.DID双向固定效应模型
# ==========================

model = PanelOLS(

    dependent=df["Return"],

    exog=df[
        [
            "DID"
        ]
    ],

    entity_effects=True,   # 企业固定效应

    time_effects=True      # 时间固定效应

)


result = model.fit(
    cov_type="clustered",
    cluster_entity=True
)



# ==========================
# 4.输出结果
# ==========================


print("===================")

print(result.summary)


# 保存结果

with open(







    "DID_regression_result.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        str(result.summary)
    )


print("===================")

print("回归结果保存4   "
      ""
      "成功")