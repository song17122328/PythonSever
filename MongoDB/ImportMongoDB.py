# -*- coding: UTF-8 -*-
"""
@Introduce:将数据导入MongoDB
@Project ：PythonSever
@File ：GetExcStruct.py
@Author ：小小小松
@Date ：2023/3/21 11:36
"""

from pymongo import MongoClient

from data import DataBase as DB


def InsertMongoDB(collection, data):
    """
    将数据插入MongoDB数据库

    :param:collection--集合名
    :param:data--数据
    :return: 无
    """
    # 建立 MongoDB 连接
    client = MongoClient(DB.URL)
    db = client[DB.DataBaseName]
    DB_collection = db[collection]
    print(data)
    # 将数据插入到 MongoDB 中
    DB_collection.insert_many(data)

    # 关闭 MongoDB 连接
    client.close()



