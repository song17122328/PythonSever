# -*- coding: UTF-8 -*-
"""
@Intorduce：冗余消除页面路由
@Project ：PythonSever 
@File ：RedundancyElimination_router.py
@Author ：小小小松
@Date ：2023/5/15 13:48
"""
import json

from flask import Blueprint, request, jsonify
from RedundancyElimination.Detection import Detection

redundancyElimination_bp = Blueprint('re_bp', __name__)


@redundancyElimination_bp.route('/redundancy_elimination', methods=['POST'])
def redundancy_elimination():
    data = request.json
    ResDict = Detection(data)
    # jsonify 是 Flask 提供的用于生成带有正确 MIME 类型和 HTTP 头部的 JSON 响应对象的简便函数。
    return jsonify(ResDict)
