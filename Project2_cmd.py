#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

def Button_3_onCommand(uiName,widgetName):
    sys.path.append("D:/000博士二下学期/TKinterDesigner-v1.6.7-win64/Project2")
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import xuanzhi
    xuanzhi.xuanzhi(topLevel)
    tkinter.Tk.wait_window(topLevel)
    InputDataArray=xuanzhi.Fun.GetInputDataArray(uiName)
    print(InputDataArray)
    pass
def Button_4_onCommand(uiName,widgetName):
    sys.path.append("D:/000博士二下学期/TKinterDesigner-v1.6.7-win64/Project2")
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import xuanxian
    xuanxian.xuanxian(topLevel)
    tkinter.Tk.wait_window(topLevel)
    InputDataArray=xuanxian.Fun.GetInputDataArray(uiName)
    print(InputDataArray)
    pass
