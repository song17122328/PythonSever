# -*- coding: UTF-8 -*-
"""
@Introduce：冗余检测
@Project ：PythonSever 
@File ：Detection.py
@Author ：小小小松
@Date ：2023/5/15 11:36
"""
import json


def find_duplicate_nodes(node, duplicates, deep=1, seen=None, path=None, ):
    """
    递归地检查重复的节点，并记录它们的位置
    """
    if seen is None:
        seen = set()
    if path is None:
        path = []

    node_name = node["nodeName"]
    node_path = path + [node_name]
    node_path_str = "->".join(node_path)
    # 如果节点已经出现过，将其添加到重复节点列表中
    if node_name not in duplicates:
        duplicates[node_name] = {}
    if node_name in seen:
        duplicates[node_name]['isRepeat'] = True

    else:
        seen.add(node_name)
        duplicates[node_name]['isRepeat'] = False
        duplicates[node_name]['detail'] = list()

    duplicates[node_name]['detail'].append({
        "path": node_path_str,
        "id": node["_id"],
        "deep": deep,
        "childrenNum": 0 if node.get("children", []) is None else len(node.get("children", []))})
    if node.get("children", []) is not None:
        for child in node.get("children", []):
            find_duplicate_nodes(node=child, duplicates=duplicates,
                                 deep=deep + 1, seen=seen, path=node_path)


def Detection(data):
    ResDict = {}
    find_duplicate_nodes(data, duplicates=ResDict)
    return ResDict


if __name__ == "__main__":
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        duplicates = {}
        find_duplicate_nodes(data, duplicates=duplicates)
        print(json.dumps(duplicates))
