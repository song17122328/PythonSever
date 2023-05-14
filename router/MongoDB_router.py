# -*- coding: UTF-8 -*-
"""
@Intorduce：
@Project ：PythonSever 
@File ：MongoDB_router.py
@Author ：小小小松
@Date ：2023/5/8 21:30
"""

from flask import Blueprint, request

import MongoDB.ImportMongoDB as mongoDB

mongoDB_bp = Blueprint('MongoDB_BP', __name__)


@mongoDB_bp.route('/TreeStructData', methods=['POST'])
def PostTreeStructDataToMongoDB():
    data = request.json
    mongoDB.InsertMongoDB("TreeStruct",data)

    return "Data received and saved to MongoDB"
