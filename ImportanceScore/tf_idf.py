# -*- coding: UTF-8 -*-
"""
@Intorduce：
@Project ：PythonSever 
@File ：index.py
@Author ：小小小松
@Date ：2023/5/14 16:09
"""
import os

import numpy as np
import pandas as pd
# %%
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import date


def GetDescriptors(file):
    # print(file)
    list_origin_word_group_ = []
    list_origin_word_group_with_allwords = []

    if type(file) == str:
        file = open(file, 'r', encoding='UTF-8')

    for line in file:
        line.lstrip()
        line = line.replace('\n', '')
        line = line.replace('\o', '')
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.lower()

        # 这边处理的列表用于最后保存于excel中
        list_origin_word_group_with_allwords.append(line)
        list_origin_word_group_with_allwords = [i for i in list_origin_word_group_with_allwords if i != '']

        list_origin_word_group_.append(line)
        list_origin_word_group_ = [i for i in list_origin_word_group_ if i != '']
    # print(list_origin_word_group_)
    return list_origin_word_group_


# 去停用词
def delete_stop_words(list_origin_word_group_):
    # 去除列表中的of和to
    list_origin_word_group = []
    for i in list_origin_word_group_:
        x = i.split()
        #  for j in x:
        #      if j == 'of' or j == 'to' or j == 'in' or j == 'li':
        #          #x.pop(j)
        new_list = list(filter(lambda y: y != 'of', x))
        new_list = list(filter(lambda y: y != 'in', new_list))
        new_list = list(filter(lambda y: y != 'li', new_list))
        new_list = list(filter(lambda y: y != 'to', new_list))
        new_list = list(filter(lambda y: y != 'number', new_list))
        new_list = list(filter(lambda y: y != 'the', new_list))
        new_list = list(filter(lambda y: y != '-', new_list))
        list_origin_word_group.append(' '.join(new_list))
        # 将描述符中单个单词拿出来并转换成列表
        vocabulary = ''
        for i in list_origin_word_group:
            vocabulary += i + ' '
        vocabulary = vocabulary.split()
        vocabulary = set(vocabulary)
        vocabulary = list(vocabulary)
    return vocabulary, list_origin_word_group


# 读取文档并清洗文本，得到所有语料库
def readPaper(dirs):
    List = os.listdir(dirs)
    Erroe_list = []
    corpus = []
    corpus_ = []

    # 将文件名和路径全部导入到列表中
    for i in range(len(List)):
        List[i] = dirs + "/" + List[i]

    # 将所有的文本导入语料库
    for fileName in List:
        try:
            a = ''
            with open(fileName, 'r', encoding='UTF-8')as f:
                for line in f:
                    a += line
            b = a.replace('\n', ' ')
            corpus.append(b)
        except:
            Erroe_list.append(fileName)
            pass
    # 得到所有语料库
    for i in corpus:
        c = i.lower()
        corpus_.append(c)
    return corpus_


def train(vocabulary, corpus_):
    # 训练模型，并转换成稀疏矩阵
    vectorizer = TfidfVectorizer(vocabulary=vocabulary, token_pattern=r'(?u)\b\w+\b')  # token_pattern = "”(?u)\b\w+\b”
    X = vectorizer.fit_transform(corpus_)
    Y = X.toarray()
    # 处理矩阵转化为dataframe
    ar = list(map(list, zip(*Y)))
    # 将所有的单词与其tf-idf值转化为字典形式，以便保存于datafarame中
    dic_ = {}
    for i in range(len(vocabulary)):
        dic_[vocabulary[i]] = ar[i]
    df_vocabulary = pd.DataFrame(dic_)
    return df_vocabulary


def getImportanceScore(df_vocabulary, list_origin_word_group, ScorePath):
    # 处理数据
    df_vocabulary.sum()
    # 得到每个单词在所有单词中的权重（softmax）
    series_v = df_vocabulary.sum() / df_vocabulary.sum().sum()
    # j计算每个节点的重要度
    dict_score = {}
    for i in list_origin_word_group:
        list_word = i.split()

        score = 0
        for j in list_word:
            score += series_v[j]

        score = score / len(list_word)  # 每个描述符除以词长
        dict_score[i] = score
    # 描述符重要度的归一化处理
    dict_score_normalization = {}
    sum_dict_score = 0

    # 得到所有描述符的重要度之和
    for i in dict_score:
        sum_dict_score += dict_score[i]

    for i in dict_score:
        dict_score_normalization[i] = dict_score[i] / sum_dict_score
    # 保存字典到excel中
    # 提取字典中的两列值key是键值，value是dict_score_normalization【key】对应的值
    key = list(dict_score_normalization.keys())
    value = list(dict_score_normalization.values())

    # 利用pandas模块先建立DateFrame类型，然后将两个上面的list存进去
    result_excel = pd.DataFrame()
    result_excel["描述符"] = key
    result_excel["TF-IDF重要度得分"] = value
    # 写入excel和csv中
    result_excel.to_excel(ScorePath)

    # 进一步处理为0，0.5和1分


def dividedThreeCategories(ScorePath, AllPath):
    data = pd.read_excel(ScorePath)
    data = data.drop(data.columns[0], axis=1)  # 去除第一列无用的数据  # 去除第一列无用的数据
    # 三分位数
    data_TFIDF = data['TF-IDF重要度得分']

    # 下1/3位数
    a1 = np.percentile(data_TFIDF, 33)

    # 上1/3位数
    a2 = np.percentile(data_TFIDF, 66)
    data_top = data.loc[data['TF-IDF重要度得分'] > a2]
    data_mid = data.loc[(a2 >= data['TF-IDF重要度得分']) & (data['TF-IDF重要度得分'] >= a1)]
    data_down = data.loc[data['TF-IDF重要度得分'] < a1]
    # 生成一个列表，把得到的重要度分成0，0.5和1 并插入到dataframe中
    list_ = []
    for i in range(data.shape[0]):
        if i in data_top.index:
            list_.append(1)
        if i in data_mid.index:
            list_.append(0.5)
        if i in data_down.index:
            list_.append(0)
    data_TFIDF_tr = data
    data_TFIDF_tr.insert(2, '三分位数', value=list_)

    data_TFIDF_tr.to_excel(AllPath)


def ReturnScore(word):
    """

    :rtype: object
    """
    dirs = "data/TF-IDF/result_literatures"
    list_origin_word_group_ = GetDescriptors(word)
    vocabulary, list_origin_word_group = delete_stop_words(list_origin_word_group_=list_origin_word_group_)
    # 得到语料库
    corpus = readPaper(dirs)
    # vocabulary为接收的描述符
    df_vocabulary = train(vocabulary, corpus)
    ScorePath = "data/TF-IDF/result_score.xlsx"
    AllPath = "data/TF-IDF/result_all.xlsx"
    getImportanceScore(df_vocabulary, list_origin_word_group, ScorePath)
    dividedThreeCategories(ScorePath, AllPath)
    return AllPath


def ReturnDescriptors():
    ScorePath = "data/TF-IDF/result_score.xlsx"
    data = pd.read_excel(ScorePath)
    data = data.drop(data.columns[0], axis=1)  # 去除第一列无用的数据  # 去除第一列无用的数据
    # 三分位数
    data_TFIDF = data['TF-IDF重要度得分']

    # 上1/3位数
    a2 = np.percentile(data_TFIDF, 66)
    data_top = data.loc[data['TF-IDF重要度得分'] > a2]
    des = data_top['描述符'].values.tolist()
    return des


if __name__ == '__main__':
    words = "data/TF-IDF/descriptors_NEW_drop.txt"
