# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-15 09:42  
# software  :python_learn 

import xlrd,os,xlwt
import collections
#excel数据处理
class DealXlsElement():
    def __init__(self,sheet_name,path='taskDeliver.xlsx'):
        self.sheet_name= sheet_name
        self.path=path

    def setSheetName(self, sheet_name):
        self.sheet_name = sheet_name

    def setPath(self, path):
        self.path = path

    def dealxlselement(self,kind,column=0):
        #kind 1表示获取字典,2为获取二维列表，column表示列
        #字典形式
        InputElement = collections.OrderedDict()
        data = xlrd.open_workbook(self.path)
        #读取参数表
        try:
            table = data.sheet_by_name(self.sheet_name)
        except:
            table = data.sheet_by_index(0)
        # 通过索引顺序获取工作表
        if kind =='dict':
            for i in range(table.nrows):
                InputElement[table.cell(i, column).value] = table.cell(i, column+1).value
            return InputElement
        elif kind=='list':
            rows=[]
            for i in range(table.nrows):
                rows.append(table.row_values(i))
            return rows

    def style_excel(self,name, height,color=0, bond=False, bord=False, background=False,wrap=False,HORZ_CENTER=True):
        style = xlwt.XFStyle()  # 可以设置6个样式类，font,borders,aligment,pattern,protection,num_format_str
        # public.字体样式
        font = xlwt.Font()
        font.height = height  # 默认高度
        font.italic = False  # 默认不设置斜体,true为开启
        font.name = name  # 字体名字'Times New Roman'
        font.bold = bond
        font.colour_index =color  #0 = Black, public = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,  the list goes on
        style.font = font
        # 2.边框
        if bord == True:
            borders = xlwt.Borders()
            borders.left = borders.THIN
            borders.right = borders.THIN  # DASHED虚线，NO_LINE没有，THIN实线，也可写数字
            borders.top = borders.THIN
            borders.bottom = borders.THIN
            style.borders = borders
        # 3.aligment设置
        aligment = xlwt.Alignment()
        aligment.vert = aligment.VERT_CENTER  # 垂直居中
        if HORZ_CENTER==True:
            aligment.horz = aligment.HORZ_CENTER  # 水平居中
        if wrap==False:
            aligment.wrap = aligment.WRAP_AT_RIGHT  # 自动换行
        else:
            pass
        style.alignment = aligment
        # 4.背景色pattern
        if background == True:
            pattern = xlwt.Pattern()
            pattern.pattern = pattern.SOLID_PATTERN  # Create the Pattern
            pattern.pattern_fore_colour = 5  ## May be: 8 through 63. 0 = Black, public = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray
            style.pattern = pattern
        return style


if __name__ == "__main__":
    a=DealXlsElement('需求单参数').dealxlselement('dict', 1)
    a.get('责任人')
    print(a.get('责任人'))
