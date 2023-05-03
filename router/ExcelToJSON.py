# -*- coding: UTF-8 -*-
"""
@Intorduce：负责把excel文件转成JSON的flask蓝图，里面有一些路由处理
@Project ：PythonSever 
@File ：ExcelToJSON.py
@Author ：小小小松
@Date ：2023/5/1 13:51
"""
import json

import pandas as pd
from flask import Blueprint, request, jsonify

from ExcelProcess.NestedTree_ExcelToJSON import ReadExcelAndReturnJSON

ExcelToJSON_bp = Blueprint('ExcelToJSON', __name__)


# POST请求接受excel，Excel为嵌套的描述符树，把Excel转成嵌套的JSON数据
@ExcelToJSON_bp.route('/TreeStruct', methods=['POST'])
def PostTreeStructToJSON():
    excel = request.files['file']
    JSON = ReadExcelAndReturnJSON(excel)
    return JSON


# POST请求接受excel，Excel为结构化描述符树信息，把Excel转成JSON数据
@ExcelToJSON_bp.route('/TreeInfo', methods=['POST'])
def PostTreeInfoToJSON():
    df = pd.read_excel(request.files['file'])
    JSON = json.dumps(df)
    return JSON

