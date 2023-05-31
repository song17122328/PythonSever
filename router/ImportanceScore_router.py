# -*- coding: UTF-8 -*-
"""
@Intorduce：重要度评分相关路由
@Project ：PythonSever 
@File ：ImportanceScore_router.py
@Author ：小小小松
@Date ：2023/5/14 18:00
"""
import json

from flask import Blueprint, request, send_file, make_response, jsonify

from ImportanceScore.tf_idf import ReturnDescriptors, ReturnScore
from ImportanceScore.formula import GetData as formulaData
from ImportanceScore.available import GetData as availableData
from ImportanceScore.heat_map import createRePic as RePic
from ImportanceScore.pie_chart import createBingPic as BingPic

importanceScore_bp = Blueprint('ImportanceScore_BP', __name__)


@importanceScore_bp.route('/TF_IDF_Score', methods=['POST'])
def PostImportanceDownload():
    data = request.json
    AllPath = ReturnScore(data)
    # 创建响应对象
    response = make_response(send_file(AllPath, as_attachment=True, mimetype='application/octet-stream'))
    return response


# @importanceScore_bp.route('/TF_IDF_Des', methods=['Get'])
# def GetImportanceDownload():
#     Descriptors = ReturnDescriptors()
#     Descriptors = json.dumps(Descriptors)
#     return Descriptors

@importanceScore_bp.route('/Available_Score', methods=['GET'])
def GetAvailable_Score():
    # 读取Excel文件
    res = availableData()
    # 返回JSON格式的数据
    return jsonify(res)


@importanceScore_bp.route('/Formula_Score', methods=['GET'])
def GetFormula_Score():
    # 读取Excel文件
    res = formulaData()
    # 返回JSON格式的数据
    return jsonify(res)


@importanceScore_bp.route('/RePic', methods=['GET'])
def GetRePic():
    RePic()
    # 返回JSON格式的数据
    return jsonify(True)


@importanceScore_bp.route('/BingPic', methods=['GET'])
def GetBingPic():
    BingPic()
    # 返回JSON格式的数据
    return jsonify(True)
