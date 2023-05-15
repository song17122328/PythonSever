# -*- coding: UTF-8 -*-
"""
@Intorduce：把excel文件转成json
@Project ：_init_.py 
@File ：NestedTree_ExcelToJSON.py
@Author ：小小小松
@Date ：2023/4/30 18:28
"""
import json
import pandas as pd
import uuid


def ReceivePathReturnJSON(path):
    # sheet_name=None,则panda会读取所有的sheet，并以字典列表的方式存储df
    # 先检测是否有合并单元格

    df = pd.read_excel(path, sheet_name=None)
    # 获取所有 sheet 的名称
    sheet_names = df.keys()
    nested_JSONs = []
    structured_JSONs = []

    for (i, name) in enumerate(sheet_names):
        data = df[name].values
        nested_data, structured_data = ReadDataAndReturnDitc(data)
        for key, value in nested_data.items():
            value["TreeType"] = name
            nested_JSONs.append(value)
            structured_JSONs.append([])
            for node in structured_data:
                node["TreeType"] = name
                structured_JSONs[i].append(node)

    dictData = {"nested_JSON": nested_JSONs, "structured_JSON": structured_JSONs}
    dictData = json.dumps(dictData)
    return dictData


def ReadDataAndReturnDitc(data):
    """
    该函数读取一个excel文件，并返回符合要求的嵌套的JSON数据
    :param path: 输入excel的路径
    :return: root_dict 为符合嵌套的JSON数据
    """

    root_dict = {}
    # 以下这个for循环堪称我遇到的最牛B的代码，出自chatGPT
    for row in data:
        # current_dict指针指向root_dict的同一块地址单元，之后修改current_dict的值，就相当于修改root_dict的孩子的值。
        current_dict = root_dict
        for value in row:
            if value != value:
                continue
            if value not in current_dict:
                ID = str(uuid.uuid4())
                # id为独一无二的uuid，对于该namespace_uuid和name下
                current_dict[value] = {"id": ID, "nodeName": value.lower(), "children": {}}
            #     此处把current_dict的地址指向current_dict[value]["children"]的地址，
            #     所以下一个for修改 current_dict[value]，相当于修改current_dict[value]["children"][value]
            current_dict = current_dict[value]["children"]

    # print(current_dict)
    # 给根节点增加"父节点ID"属性
    add_parent_id(root_dict)

    # print(root_dict)
    structured_data = convert_nested_dict_to_structured_data(root_dict)
    # 把字典类型的数据转成符合要求的嵌套数据
    nested_data = convert_dict_to_list(root_dict)

    return nested_data, structured_data


def add_parent_id(dic, parent_id=""):
    if isinstance(dic, dict):
        for key, value in dic.items():
            value.update({'parentID': parent_id})
            add_parent_id(value['children'], value['id'])


# 修改字典中子节点的类型为列表
def convert_dict_to_list(data_dict):
    for key, value in data_dict.items():
        if isinstance(value, dict) and "children" in value:
            value["children"] = convert_dict_to_list(value["children"])
            data_dict[key] = value
            value["children"] = list(value["children"].values())
    return data_dict


def convert_nested_dict_to_structured_data(nested_dict, parent_id=''):
    """
    该函数将嵌套的字典数据转化成结构化的数据
    :param nested_dict: 嵌套的字典数据
    :param parent_id: 父节点ID，初始值为''
    :return: 结构化的数据列表，包含id, nodeName, parentID, childrenID, childrenName等属性
    """

    structured_data_list = []

    for key, value in nested_dict.items():
        node_id = value['id']
        node_name = value['nodeName']
        children_ids = []
        children_names = []

        for child_key, child_value in value['children'].items():
            child_id = child_value['id']
            child_name = child_value['nodeName']
            children_ids.append(child_id)
            children_names.append(child_name)

            structured_data_list += convert_nested_dict_to_structured_data(
                {child_key: child_value},
                parent_id=node_id
            )

        structured_data_list.append({
            '_id': node_id,
            'NodeName': node_name,
            'ParentId': parent_id,
            'ChildrenId': children_ids,
            'ChildrenName': children_names
        })

    return structured_data_list


def convert_nested_Tree_to_structured_list(nested_dict, parent_id=''):
    """
    该函数将嵌套的字典数据转化成结构化的数据
    :param nested_dict: 嵌套的字典数据
    :param parent_id: 父节点ID，初始值为''
    :return: 结构化的数据列表，包含id, nodeName, parentID, childrenID, childrenName等属性
    """

    structured_data_list = []
    node_id = nested_dict['id']
    node_name = nested_dict['nodeName']
    node_type=nested_dict['treeType']
    children_ids = []
    children_names = []

    if nested_dict['children'] is not None:
        for child_value in nested_dict['children']:
            child_id = child_value['id']
            child_name = child_value['nodeName']
            children_ids.append(child_id)
            children_names.append(child_name)
            structured_data_list += convert_nested_Tree_to_structured_list(
                child_value,
                parent_id=node_id
            )

    structured_data_list.append({
        '_id': node_id,
        'NodeName': node_name,
        'ParentId': parent_id,
        'TreeType':node_type,
        'ChildrenId': children_ids,
        'ChildrenName': children_names,
        'from':nested_dict['from']

    })

    return structured_data_list


# 主函数为测试案例
if __name__ == '__main__':
    path = "../data/data1.xlsx"

    res = ReceivePathReturnJSON(path)

    # print(flatten_tree(res))
    # for item in begin(path):
    #     print(item)
    # print(begin(path))
