# -*- coding: UTF-8 -*-
"""
@Intorduce：重要度评分相关路由
@Project ：PythonSever 
@File ：ImportanceScore_router.py
@Author ：小小小松
@Date ：2023/5/14 18:00
"""
from flask import Blueprint, request, send_from_directory, send_file, make_response

from ImportanceScore.tf_idf import GetAll,GetScore

importanceScore_bp = Blueprint('ImportanceScore_BP', __name__)


@importanceScore_bp.route('/TF_IDF_Score', methods=['POST'])
def PostTF_IDF_Score():
    data = request.json
    ScorePath = GetScore(data)
    # 创建响应对象
    response = make_response(send_file(ScorePath, as_attachment=True, mimetype='application/octet-stream'))

    return response


@importanceScore_bp.route('/TF_IDF_All', methods=['POST'])
def PostImportanceDownload():
    data = request.json
    AllPath = GetAll(data)
    return send_from_directory(AllPath, AllPath, as_attachment=True)


