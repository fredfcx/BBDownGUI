from tkinter import ttk
from tkinter import *
import os

api = "null"
mode = "null"
def ddanmu():
    global mode
    mode = " -dd"
def app():
    global api
    api = " -app"

def tv():
    global api
    api = " -tv"


def download():
    if api == "null":
        SJBVLink = BVLink.get()
        os.system("BBDown "+SJBVLink+mode)
    elif mode == "null":
        if api == "null":
           SJBVLink = BVLink.get()
           os.system("BBDown "+SJBVLink) 
        else:
            SJBVLink = BVLink.get()
            os.system("BBDown "+SJBVLink+api)
    else:
        SJBVLink = BVLink.get()
        os.system("BBDown "+SJBVLink+api+mode)


root = Tk()
main = ttk.Frame(root)
BVLink = StringVar()
Text1 = ttk.Label(main,text="请输入BV号或视频链接：")
Text1.pack()
BVLinkInput = ttk.Entry(main,width=20,textvariable=BVLink)
BVLinkInput.pack()
Text2 = ttk.Label(main,text="解析方式：")
Text2.pack()
ModeButton1 = ttk.Radiobutton(main,text="默认(电脑端)",value="mode1")
ModeButton1.pack()
ModeButton2 = ttk.Radiobutton(main,text="手机端(APP)",value="mode2",command=app)
ModeButton2.pack()
ModeButton3 = ttk.Radiobutton(main,text="电视端(无水印)",value="mode3",command=tv)
ModeButton3.pack()
ButtonOK = ttk.Button(main,text="执行",command=download)
downloaddd = ttk.Checkbutton(main,text="同时下载弹幕",onvalue="danmu_on",offvalue="danmu_off",command=ddanmu)
ButtonOK.pack()
downloaddd.pack()
main.grid()
root.mainloop()