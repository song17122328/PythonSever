# -*- coding: UTF-8 -*-
"""
@Introduce：获取可获得描述符表
@Project ：NestedTree_ExcelToJSON.py 
@File ：available.py
@Author ：小小小松
@Date ：2023/5/26 23:47
"""
import pandas as pd


def GetData():
    Path = "data/基于可获得性/可获得描述符表.xlsx"
    res = pd.read_excel(Path)
    res = set(res['描述符'])
    # 将数据转换为字典格式
    # res = res.to_dict(orient='records')
    return list(res)
