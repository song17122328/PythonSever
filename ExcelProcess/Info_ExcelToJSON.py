# -*- coding: UTF-8 -*-
"""
@Intorduce：
@Project ：PythonSever 
@File ：Info_ExcelToJSON.py
@Author ：小小小松
@Date ：2023/5/5 12:12
"""

import json
import math

import pandas as pd


def ReceivePathReturnJSON(path):
    df = pd.read_excel(path)
    df = df.fillna('')
    JSON = df.to_dict('records')
    json_data = json.dumps(JSON)

    return json_data


def replace_nan(obj):
    if isinstance(obj, float) and math.isnan(obj):
        return "NaN"
    else:
        return obj
