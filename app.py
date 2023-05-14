# -*- coding: UTF-8 -*-
"""
@Intorduce：Flask服务器的入口程序，负责蓝图注册和服务器启动
@Project ：PythonSever 
@File ：app.py
@Author ：小小小松
@Date ：2023/5/1 14:12
"""
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# 如果您只想允许特定的域名，请将CORS实例化时的origin参数设置为您允许的域名。例如：只允许来自http://localhost:7081域名的请求。
# 如果不写origins，则所有域名均可以访问.supports_credentials=True可以让前端界面接收到返回的数据
CORS(app,supports_credentials=True)

# 导入处理Excel成JSON的蓝图
from router.ExcelToJSON_router import ExcelToJSON_bp
from router.MongoDB_router import mongoDB_bp
from router.ImportanceScore_router import importanceScore_bp

app.register_blueprint(ExcelToJSON_bp)
app.register_blueprint(mongoDB_bp)
app.register_blueprint(importanceScore_bp)
