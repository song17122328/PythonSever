# -*- coding: UTF-8 -*-
"""
@Intorduce：
@Project ：_init_.py 
@File ：__init__.py.py
@Author ：小小小松
@Date ：2023/4/30 23:52
"""

# 此文件提供一些必要的信息

# 孙拾雨的论文地址
SunPaperPath = "D:\yxs\课程\大四\毕设\Data\孙拾雨. 基于描述符树的NASICON型固态电解质离子输运构效关系研究.pdf"
DataPath = "../../Data"


# Excel源数据所在的位置及对应的表格名
class Data:
    # 描述符树所在的地址
    DescriptorsTreePath = "D:\yxs\课程\大四\毕设\Data\描述符树数据.xlsx"
    DescriptorsTreeSheetName = "DBdata"
    MLforDescriptorPath = "D:\yxs\课程\大四\毕设\Data\机器学习描述符及对应属性值.xlsx"
    MLforDescriptorSheetName = 'complete information'


# 以下是数据库连接相关信息
class DataBase:
    # 定义类属性
    URL = 'mongodb://localhost:27017/DbforNasicon'
    DataBaseName = "DbforNasicon"
    collections = ['DescriptorTree', 'MLforDescriptor']
