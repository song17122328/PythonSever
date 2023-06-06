# -*- coding: UTF-8 -*-
"""
@Introduce：
@Project ：NestedTree_ExcelToJSON.py 
@File ：可视化饼图.py
@Author ：小小小松
@Date ：2023/5/27 13:39
"""
import pandas as pd
import matplotlib.pyplot as plt


def createBingPic(data):
    # 读取Excel文件
    df = pd.DataFrame(data)
    print(df)

    # 根据Score进行分组
    grouped = df.groupby('Score')['Descriptor'].apply(list)

    # 统计每个分数的频率
    scores = grouped.index.tolist()
    frequencies = [len(descriptors) for descriptors in grouped]

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    explode = [0] * len(scores)
    for i, score in enumerate(scores):
        if score in [3.5, 3.0]:
            explode[i] = 0.2

    wedgeprops = {'width': 0.15, 'edgecolor': 'white'}

    plt.pie(frequencies, labels=scores, autopct='%1.1f%%', explode=explode, wedgeprops=wedgeprops)
    plt.title('Descriptor Scores')
    plt.axis('equal')

    # 生成图例
    handles, labels = plt.gca().get_legend_handles_labels()
    legend = plt.legend(handles, labels, loc='upper right', title='Scores')

    # 调整图例的字体大小
    for text in legend.get_texts():
        text.set_fontsize(10)

    # 导出图片

    plt.savefig('../frontend-xai-base/src/assets/pie_chart.png', dpi=800)
