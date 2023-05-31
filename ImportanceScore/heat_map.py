# -*- coding: UTF-8 -*-
"""
@Introduce：
@Project ：NestedTree_ExcelToJSON.py 
@File ：热力图.py
@Author ：小小小松
@Date ：823/5/27 14:02
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import textwrap


def createRePic():
    # 读取Excel文件
    df = pd.read_excel('data/各描述符得分及综合评分(排序).xlsx')
    descriptor = df['Descriptor']
    score = df['Score']
    descriptorData = []
    scoreData = []
    for i in range(40):
        tempDesp = []
        tempScore = []
        for j in range(8):
            tempDesp.append(descriptor[i * 8 + j])
            tempScore.append(score[i * 8 + j])
        descriptorData.append(tempDesp)
        scoreData.append(tempScore)
    descriptorData = np.array(descriptorData)
    scoreData = np.array(scoreData)

    # 调整图像尺寸
    plt.figure(figsize=(20, 20))

    # 绘制热力图
    ax = sns.heatmap(scoreData, cmap='YlGnBu', annot=descriptorData, fmt='', cbar=True, cbar_kws={'label': 'Score'})
    ax.set_title('Score Heatmap')

    # 调整注释文字大小和换行
    for text in ax.texts:
        wrapped_text = textwrap.fill(text.get_text(), 24)
        text.set_text(wrapped_text)
        text.set_fontsize(8)

    # 隐藏刻度
    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('D:/yxs/课程/大四/毕设/WorkCode/frontend-xai-base/src/assets/Score_Heatmap.png', dpi=300)
