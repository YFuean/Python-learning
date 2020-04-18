'''
excel操作,生成词云
'''

import xlrd
import wordcloud
import random


def make(fileName, sheetName):
    # 打开工作簿
    workbook = xlrd.open_workbook('./res/excel/'+fileName)
    # 根据名字获取sheet
    sheet = workbook.sheet_by_name(sheetName)

    # 获取单元格，行i，列j
    cells = []
    for j in range(1, sheet.ncols):
        for i in range(1, sheet.nrows):
            cell = sheet.cell(i, j).value
            cells.append(cell)

    # print(cells)
    # 生成词云
    w = wordcloud.WordCloud(
        width=1000,
        height=700,
        background_color='#70d0b2',
        colormap='PuBu',
        font_path='./res/fonts/SimHei.ttf')

    result = ','.join(cells)
    w.generate(result)
    w.to_file('./res/img/班级表词云.png')


if __name__ == "__main__":
    make('班级卡片数据.xlsx', '工作表1')
