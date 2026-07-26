import pandas as pd
import numpy as np

from statsmodels.stats.outliers_influence import variance_inflation_factor


# =========================
# 1.读取DID数据
# =========================

df = pd.read_excel(
    "DID_stock_data.xlsx"
)


print("数据读取成功")

print(df.head())


# =========================
# 2.相关性分析
# =========================

corr = df[
    [
        "Return",
        "NEV",
        "Policy",
        "DID"
    ]
].corr()


print("================")
print("相关性矩阵")
print(corr)


# 保存相关矩阵

corr.to_excel(
    "correlation_matrix.xlsx"
)


# =========================
# 3.VIF多重共线性检验
# =========================


X = df[
    [
        "NEV",
        "Policy",
        "DID"
    ]
]


# 添加常数项

X["const"] = 1


vif = pd.DataFrame()


vif["变量"] = X.columns


vif["VIF"] = [
    variance_inflation_factor(
        X.values,
        i
    )
    for i in range(
        X.shape[1]
    )
]


print("================")
print("VIF检验结果")
print(vif)


# 保存

vif.to_excel(
    "VIF_result.xlsx",
    index=False
)


print("保存成功")