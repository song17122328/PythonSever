# -*- coding: UTF-8 -*-
"""
@Introduce:提取论文中的描述符结构
    输入：如下四个文件，为拆分单元格后的树结构表
    'D:\yxs\课程\大四\毕设\Data\专家经验树_.xlsx'
    'D:\yxs\课程\大四\毕设\Data\文本挖掘树_.xlsx'
    'D:\yxs\课程\大四\毕设\Data\融合树_.xlsx'
    'D:\yxs\课程\大四\毕设\Data\机器学习特征树_.xlsx'
    输出：'描述符树结构表.xlsx'。
    注意：运行完程序得到'描述符树结构表.xlsx'

@Project ：PythonSever
@File ：GetExcStruct.py
@Author ：小小小松
@Date ：2023/3/20 11:16
"""
import os

import pandas as pd

from data._init_ import DataPath


def GetDataFrame(path, type):
    """
    把表格的信息提取成字典列表，最后统一转成dataframe插入excel中。

    输入源表格，输出List<dict>对象，

    :param path: 待处理Excel文件的地址，此处为'专家经验树_.xlsx','文本挖掘树_.xlsx','机器学习特征树_.xlsx','融合树_.xlsx'
    :param type: 文件对应的树种类，如'专家经验树_.xlsx' 对应为"expert", '机器学习特征树_.xlsx' 对应为“feature”
    :return: 字典组成的列表：List[dict]
    """

    df = pd.read_excel(path)
    values = df.values

    List = []

    for j in range(values.shape[1]):
        # 按列遍历
        dic = {"RootName": values[0][0], 'NodeName': None, 'ChildArray': set(), 'LevelHierarchy': None, 'Type': type}
        for i in range(values.shape[0]):
            # 空值跳出
            if values[i, j] != values[i, j]:
                continue
            # 最后一层结点，且非空结点，没有孩子数组
            if j == values.shape[1] - 1:
                dic = {"RootName": values[0][0], 'NodeName': values[i, j], 'ChildArray': None,
                       'LevelHierarchy': str(j + 1),
                       'Type': type}
                List.append(dic)
                continue

            # 非最后一层结点，可能有孩子结点
            # 相同结点：添加孩子数组操作
            if i == 0:
                dic['NodeName'] = values[i, j]
                dic['LevelHierarchy'] = str(j + 1)
                dic['ChildArray'].add(values[i, j + 1])
                continue
            if dic['NodeName'] == values[i, j]:
                dic['ChildArray'].add(values[i, j + 1])
                continue
            # 不同数组，新建立结点和孩子数组
            if dic['NodeName'] != values[i, j]:
                dic['ChildArray'] = list(dic['ChildArray'])
                List.append(dic)
                # print(NodeName, ":", ChildArray)
                dic = {"RootName": values[0][0], 'NodeName': values[i, j], 'ChildArray': set(),
                       'LevelHierarchy': str(j + 1),
                       'Type': type}
                dic['ChildArray'].add(values[i, j + 1])
        if j != values.shape[1] - 1:
            dic['ChildArray'] = list(dic['ChildArray'])
            List.append(dic)

    return List


if __name__ == '__main__':
    excels = ['专家经验树_.xlsx', '文本挖掘树_.xlsx', "机器学习特征树_.xlsx", '融合树_.xlsx']
    Type = ['expert', 'textMining', 'feature', 'fusion']
    List = []
    for i in range(len(excels)):
        path = os.path.join(DataPath, excels[i])
        type = Type[i]
        List.extend(GetDataFrame(path, type))
    dfres = pd.DataFrame(List)

    dfres.to_excel("描述符树结构表.xlsx", index=False)

    # 把里面的['nan']，替换成空值
    replaceRes = pd.read_excel("描述符树结构表.xlsx")
    replaceRes.replace('[nan]', '', inplace=True)
    replaceRes.to_excel("描述符树结构表.xlsx", index=False)
