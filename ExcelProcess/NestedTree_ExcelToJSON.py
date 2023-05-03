# -*- coding: UTF-8 -*-
"""
@Intorduce：把excel文件转成json
@Project ：_init_.py 
@File ：NestedTree_ExcelToJSON.py
@Author ：小小小松
@Date ：2023/4/30 18:28
"""
import json
import os
from data._init_ import DataPath
import pandas as pd


def ReadExcelAndReturnJSON(path):
    """
    该函数读取一个excel文件，并返回符合要求的嵌套的JSON数据
    :param path: 输入excel的路径
    :return: root_dict 为符合嵌套的JSON数据
    """
    df = pd.read_excel(path)
    data = df.values

    id_counter = 1  # 设置计数器以生成唯一id

    root_dict = {}
    # 以下这个for循环堪称我遇到的最牛B的代码，出自chatGPT
    for row in data:
        # current_dict指针指向root_dict的同一块地址单元，之后修改current_dict的值，就相当于修改root_dict的孩子的值。
        current_dict = root_dict

        for value in row:
            if value != value:
                continue
            if value not in current_dict:
                current_dict[value] = {"id": str(id_counter), "nodeName": value,"children": {}, }
                id_counter += 1  # 每添加一个节点，计数器加1
            #     此处把current_dict的地址指向current_dict[value]["children"]的地址，
            #     所以下一个for修改 current_dict[value]，相当于修改current_dict[value]["children"][value]
            current_dict = current_dict[value]["children"]

    # 把字典类型的数据转成符合要求的嵌套数据
    root_dict = convert_dict_to_list(root_dict)
    json_data = json.dumps(root_dict)
    return json_data


# print(f"current_dict：{current_dict}")

# 修改字典中子节点的类型为列表
def convert_dict_to_list(data_dict):
    for key, value in data_dict.items():
        if isinstance(value, dict) and "children" in value:
            value["children"] = convert_dict_to_list(value["children"])
            data_dict[key] = value
            value["children"] = list(value["children"].values())
    return data_dict


# 主函数为测试案例
if __name__ == '__main__':
    excels = ['专家经验树_.xlsx', '文本挖掘树_.xlsx', "机器学习特征树_.xlsx", '融合树_.xlsx']
    path = os.path.join(DataPath, excels[0])
    print(ReadExcelAndReturnJSON(path))
