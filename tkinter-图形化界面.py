# -*- coding:utf-8 -*-
# author    :范佳郡
# datetime  :2019-05-04 09:36  
# software  :python_learn 
import tkinter

# 测试图形化界面是否要用
# tkinter._test()
# 定义一个面板
base = tkinter.Tk()

# 标题名称
base.wm_title('label title')

# 标签中的内容
lb = tkinter.Label(base, text = 'label text')
# 给相应的组建布局
lb.pack()

lb1 = tkinter.Label(base, text = '背景是蓝色的标签', background = 'blue')
lb1.pack()

print('pack布局**************************************************************************************')
'''
pack布局
最简单，代码量最少，挨个摆放，默认从上倒下，系统自动设置
通用使用方式为： 组件对象.pack(设置，，，，，，，）
side: 停靠方位， 可选值为LEFT,TOP,RIGHT,BOTTON
fill: 填充方式,X,Y,BOTH,NONE
expande: YES/NO
anchor: N,E,S,W,CENTER
ipadx: x方向的内边距
ipady: y
padx: x方向外边界
pady： y........
'''
btn1 = tkinter.Button(base, text='A')
btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)

btn2 = tkinter.Button(base, text='B')
btn2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

btn2 = tkinter.Button(base, text='C')
btn2.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.NONE,anchor=tkinter.NE)

btn2 = tkinter.Button(base, text='D')
btn2.pack(side=tkinter.LEFT, expand=tkinter.NO, fill=tkinter.Y)

btn2 = tkinter.Button(base, text='E')
btn2.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.BOTH)

btn2 = tkinter.Button(base, text='F')
btn2.pack(side=tkinter.BOTTOM, expand=tkinter.YES)

btn2 = tkinter.Button(base, text='G')
btn2.pack(anchor=tkinter.SE)

def showLabel():
    global base
    print('我被点击了')
    lb2 = tkinter.Label(base, text = '按钮点出来的',background = 'green')
    lb2.pack()

def anLabel(event):
    global base
    print('我被关联点击了')
    lb2 = tkinter.Label(base, text='按钮是关联点出来的',background ='blue')
    lb2.pack()

btn = tkinter.Button(base, text = '这是一个按钮', background = 'yellow' ,command =showLabel)
btn.pack()

lb2 = tkinter.Label(base, text='这是一个label关联出来的')
# label绑定相应的消息和处理函数
# 自动获取左键点击，并启动相应的处理函数baseLabel
lb2.bind("<Button - 1>",anLabel)
lb2.pack()

# 启动面板上的消息循环
base.mainloop()
print('pack布局完成**************************************************************************************')
'''
Button的属性：
anchor 				设置按钮中文字的对其方式，相对于按钮的中心位置
background(bg) 		设置按钮的背景颜色
foreground(fg)		设置按钮的前景色（文字的颜色）
borderwidth(bd)		设置按钮边框宽度
cursor				设置鼠标在按钮上的样式
command				设定按钮点击时触发的函数
bitmap				设置按钮上显示的位图
font				设置按钮上文本的字体
width				设置按钮的宽度  (字符个数)
height				设置按钮的高度  (字符个数)
state				设置按钮的状态
text				设置按钮上的文字
image				设置按钮上的图片
'''

print('grid布局********************************************************************************************')
'''
grid布局
通用使用方式：组件对象.grid(设置,,,,,,,)
利用row，column编号，都是从0开始
sticky： N,E,S,W表示上下左右，用来决定组件从哪个方向开始
支持ipadx，padx等参数，跟pack函数含义一样
支持rowspan，columnspan，表示跨行，跨列数量
'''
# 登陆提示
def logining():
    name = account.get()
    pwd = password.get()
    t1 = len(name)
    t2 = len(pwd)

    if name == 'kareen' and pwd == '123123':
        lb3['text']='登陆成功'
    else:
        lb3['text']='用户名或密码错误'
        # 输入框删除掉用户输入的内容
        # 注意delete的两个参数，表示从第几个删除到第几个
        account.delete(0, t1)
        password.delete(0, t2)

basegrid = tkinter.Tk()
basegrid.wm_title('这是登陆界面')


lbgrid1 = tkinter.Label(basegrid, text='账号: ')
lbgrid1.grid(row=1, sticky=tkinter.W)

account = tkinter.Entry(basegrid)
account.grid(row=1, column=1, sticky=tkinter.E)

lbgrid2 = tkinter.Label(basegrid, text="密码: ").grid(row=2, sticky= tkinter.W)
password = tkinter.Entry(basegrid)
password.grid(row=2, column=1, sticky=tkinter.E)
# 输入的密码显示成*号
password['show'] = '*'

# Button参数command的意思是，当按钮被点击后启动相应的处理函数
btngrid = tkinter.Button(basegrid, text="登录", command=logining).grid(row=3, column=1, sticky=tkinter.W)

lb3 = tkinter.Label(basegrid, text='')
lb3.grid(row=4)


# 新增菜单
menubar = tkinter.Menu(basegrid)
# 右键菜单,在mac上实现存在问题，暂时未实现
rightmenu = tkinter.Menu(basegrid)

# 新增菜单中的子菜单
emenu = tkinter.Menu(menubar)
emenu2 = tkinter.Menu(rightmenu)
for item in ['cut', 'paste', 'copy']:
    emenu.add_command(label=item)
    emenu2.add_command(label=item)

menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit',menu=emenu)

for item2 in ['复制', '打印', '检查']:
    rightmenu.add_separator()
    rightmenu.add_command(label=item2)
rightmenu.add_cascade(label='看看',menu=emenu2)


def pop(event):
    rightmenu.post(event.x_root,event.y_root)


basegrid.bind('<Button - 3>', pop)

basegrid['menu'] = menubar


basegrid.mainloop()

print('grid布局完成*****************************************************************************************')
'''
place布局
明确方位的摆放
相对位置布局，随意改变窗口大小会导致混乱
使用place函数，分为绝对布局和相对布局，绝对布局使用x，y参数
相对布局使用relx，rely, relheight, relwidth
'''
'''
canvas 画布
画布： 可以自由的在上面绘制图形的一个小舞台
在画布上绘制对象， 通常用create_xxxx，xxxx=对象类型， 例如line，rectangle
画布的作用是把一定组件画到画布上显示出来
画布所支持的组件：
arc
bitmap
image(BitmapImage, PhotoImage)
line
oval
polygon
rectangle
text
winodw（组件）
每次调用create_xxx都会返回一个创建的组件的ID，同时也可以用tag属性指定其标签
通过调用canvas.move实现一个一次性动作
'''
import math as m
canvasFrame = tkinter.Tk()

cvs = tkinter.Canvas(canvasFrame, width=300, height=300,background='blue')
cvs.pack()

# 一条线需要两个点指明起始
# 参数数字的单位是px
cvs.create_line(10, 10, 30, 30)

cvs.create_text(10,10, text="I LOVE PYTHON")

center_x = 150
center_y = 150

r = 150

# 依次存放五个点的位置
points = [
        #左上点
        # pi是一个常量数字，3.1415926
        center_x - int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),

        #右上点
        center_x + int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),

        #左下点
        center_x - int(r * m.sin( m.pi / 5)),
        center_y + int(r * m.cos( m.pi / 5)),

        #顶点
        center_x,
        center_y - r,

        #右下点
        center_x + int(r * m.sin(m.pi / 5)),
        center_y + int(r * m.cos(m.pi / 5)),
    ]
# 创建一个多边形
cvs.create_polygon(points, outline="red", fill="yellow")
cvs.create_text(150,150, text="五角星")

canvasFrame.mainloop()

import tkinter

baseFrame = tkinter.Tk()

def btnClick(event):
        global  w
        w.move(id_ball, 12,5)
        w.move("fall", 0,5)



w = tkinter.Canvas(baseFrame, width=500, height=400)
w.pack()
w.bind("<Button-1>", btnClick)

# 创建组件后返回id
id_ball  = w.create_oval(20,20, 50,50, fill="green")

# 创建组件使用tag属性
w.create_text(123,56, fill="red", text="ILovePython", tag="fall")
# 创建的时候如果没有指定tag可以利用addtag_withtag添加
# 同类函数还有 addtag_all, addtag_above, addtag_xxx等等
id_rectangle = w.create_rectangle(56,78,173,110, fill="gray")
w.addtag_withtag("fall", id_rectangle)


baseFrame.mainloop()