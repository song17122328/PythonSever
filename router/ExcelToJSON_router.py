# -*- coding: UTF-8 -*-
"""
@Intorduce：负责把excel文件转成JSON的flask蓝图，里面有一些路由处理
@Project ：PythonSever 
@File ：ExcelToJSON_router.py
@Author ：小小小松
@Date ：2023/5/1 13:51
"""
import json

import pandas as pd
from flask import Blueprint, request, jsonify

import ExcelProcess.NestedTree_ExcelToJSON as NestedTree
import ExcelProcess.Info_ExcelToJSON as Info
import MergeCell.MergeCellDetection as Detection
import MergeCell.MergeCellSplit as Split
import MongoDB.InitMongoDB

ExcelToJSON_bp = Blueprint('ExcelToJSON_BP', __name__)


# POST请求接受excel，Excel为嵌套的描述符树，把Excel转成嵌套的JSON数据
@ExcelToJSON_bp.route('/TreeStruct', methods=['POST'])
def PostTreeStructToJSON():
    excel = request.files['file']
    # 检测是否有合并单元格
    if Detection.HasMergedCell(excel):
        # 若有合并单元格，则全部拆分
        Split.MergeCellSplit(excel)
    data = NestedTree.ReceivePathReturnJSON(excel)
    return data


@ExcelToJSON_bp.route('/NestedToStructureToMongoDB', methods=['POST'])
def PostNestedToStructureToMongoDB():
    data = request.json
    res = list()
    if isinstance(data,list):
        for i in data:
            res.append(NestedTree.convert_nested_Tree_to_structured_list(i))
    else:
        res = NestedTree.convert_nested_Tree_to_structured_list(data)
    return jsonify(res)


# POST请求接受excel，Excel为结构化描述符树信息，把Excel转成JSON数据
@ExcelToJSON_bp.route('/TreeInfo', methods=['POST'])
def PostTreeInfoToJSON():
    excel = request.files['file']
    JSON = Info.ReceivePathReturnJSON(excel)
    return JSON
