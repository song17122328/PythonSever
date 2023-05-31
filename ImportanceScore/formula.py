# -*- coding: UTF-8 -*-
"""
@Introduce：提供基于公式的描述符关联表
@Project ：NestedTree_ExcelToJSON.py 
@File ：formula.py
@Author ：小小小松
@Date ：2023/5/26 23:47
"""
import pandas as pd


def GetData():
    Path = "data/基于公式/公式描述符关联表.xlsx"

    res = pd.read_excel(Path)
    res = set(res['描述符'])
    # 将数据转换为字典格式
    # res = res.to_dict(orient='records')
    return list(res)
