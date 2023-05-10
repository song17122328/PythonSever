# -*- coding: UTF-8 -*-
"""
@Introduce:将”描述符树结构表.xlsx“、‘描述符信息表.xlsx’、‘机器学习描述符属性值.xlsx’ 三张表插入mongoDB数据库
@Project ：PythonSever
@File ：GetExcStruct.py
@Author ：小小小松
@Date ：2023/3/21 11:36
"""
import pandas as pd
from pymongo import MongoClient

from data import DataBase as DB


def InsertMongoDB(insertData):
    """
    将数据插入MongoDB数据库

    :param insertData: dataSolve()函数返回的结果，包含3个DataFrame转成的dict对象，分别对应 "描述符树结构表.xlsx",'描述符树结构表.xlsx','描述符树结构表.xlsx'
    :return: 无
    """
    # 建立 MongoDB 连接
    client = MongoClient(DB.URL)
    db = client[DB.DataBaseName]
    TreeStruct = db['TreeStruct']
    DescriptorInfo = db['DescriptorInfo']
    MlData = db['MlData']

    # 清除集合
    TreeStruct.drop()
    DescriptorInfo.drop()
    MlData.drop()

    # 创建集合
    db.create_collection('TreeStruct')
    db.create_collection('DescriptorInfo')
    db.create_collection('MlData')
    # 将数据插入到 MongoDB 中
    TreeStruct.insert_many(insertData[0])
    DescriptorInfo.insert_many(insertData[1])
    MlData.insert_many(insertData[2])
    # 关闭 MongoDB 连接
    client.close()


def dataSolve():
    """
    数据处理

    :return:List[List[dict]] 列表包含3个DataFrame转成的dict对象，分别对应 "描述符树结构表.xlsx",'描述符树结构表.xlsx','描述符树结构表.xlsx'
    """
    # 读取 Excel 表格数据
    dfTreeStruct = pd.read_excel("描述符树结构表.xlsx")
    dfDescriptorInfo = pd.read_excel('描述符信息表.xlsx')
    dfMlData = pd.read_excel('机器学习描述符属性值.xlsx',sheet_name="complete information")
    # 处理描述符树结构表中的孩子数组
    for i, child in enumerate(dfTreeStruct.ChildArray):
        if child == child:
            child = child.replace("'", '').replace("[", '').replace("]", '')
            dfTreeStruct.ChildArray[i] = child.split(', ')
        else:
            dfTreeStruct.ChildArray[i] = None

    # 将数据转换为字典格式，存入结果集
    StructRes = dfTreeStruct.to_dict('records')
    InfoRes = dfDescriptorInfo.to_dict('records')
    MLDataRes = dfMlData.to_dict('records')
    return [StructRes, InfoRes, MLDataRes]


if __name__ == '__main__':
    data = dataSolve()
    InsertMongoDB(data)
