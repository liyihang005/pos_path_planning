#coding=utf-8
#import libs 
import sys
import xuanzhi_cmd
import xuanzhi_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  xuanzhi:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = xuanzhi_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,480,619)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 480,height = 619)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_4 = tkinter.Label(Form_1,text="限制条件",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4)
        Fun.SetControlPlace(uiName,'Label_4',27,7,168,29)
        Label_4.configure(relief = "flat")
        Label_4_Ft=tkinter.font.Font(family='System', size=20,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5 = tkinter.Entry(Form_1,textvariable=Entry_5_Variable)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Fun.SetControlPlace(uiName,'Entry_5',219,49,120,20)
        Entry_5.configure(relief = "sunken")
        Label_6 = tkinter.Label(Form_1,text="基本农田（shpfile）",width = 10,height = 4)
        Fun.Register(uiName,'Label_6',Label_6)
        Fun.SetControlPlace(uiName,'Label_6',43,81,156,20)
        Label_6.configure(relief = "flat")
        Entry_7_Variable = Fun.AddTKVariable(uiName,'Entry_7','')
        Entry_7 = tkinter.Entry(Form_1,textvariable=Entry_7_Variable)
        Fun.Register(uiName,'Entry_7',Entry_7)
        Fun.SetControlPlace(uiName,'Entry_7',221,81,120,20)
        Entry_7.configure(relief = "sunken")
        Label_8 = tkinter.Label(Form_1,text="生态红线(shpfile)",width = 10,height = 4)
        Fun.Register(uiName,'Label_8',Label_8)
        Fun.SetControlPlace(uiName,'Label_8',65,116,100,20)
        Label_8.configure(relief = "flat")
        Entry_9_Variable = Fun.AddTKVariable(uiName,'Entry_9','')
        Entry_9 = tkinter.Entry(Form_1,textvariable=Entry_9_Variable)
        Fun.Register(uiName,'Entry_9',Entry_9)
        Fun.SetControlPlace(uiName,'Entry_9',220,116,120,20)
        Entry_9.configure(relief = "sunken")
        Label_10 = tkinter.Label(Form_1,text="必选",width = 10,height = 4)
        Fun.Register(uiName,'Label_10',Label_10)
        Fun.SetControlPlace(uiName,'Label_10',-6,71,57,20)
        Label_10.configure(relief = "flat")
        Label_11 = tkinter.Label(Form_1,text="可选",width = 10,height = 4)
        Fun.Register(uiName,'Label_11',Label_11)
        Fun.SetControlPlace(uiName,'Label_11',-15,267,71,20)
        Label_11.configure(relief = "flat")
        Entry_13_Variable = Fun.AddTKVariable(uiName,'Entry_13','')
        Entry_13 = tkinter.Entry(Form_1,textvariable=Entry_13_Variable)
        Fun.Register(uiName,'Entry_13',Entry_13)
        Fun.SetControlPlace(uiName,'Entry_13',218,154,120,20)
        Entry_13.configure(relief = "sunken")
        Label_16 = tkinter.Label(Form_1,text="基本走向",width = 10,height = 4)
        Fun.Register(uiName,'Label_16',Label_16)
        Fun.SetControlPlace(uiName,'Label_16',69,231,100,20)
        Label_16.configure(relief = "flat")
        ComboBox_19_Variable = Fun.AddTKVariable(uiName,'ComboBox_19')
        ComboBox_19 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_19_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_19',ComboBox_19)
        Fun.SetControlPlace(uiName,'ComboBox_19',218,231,121,20)
        ComboBox_19.configure(state = "readonly")
        ComboBox_19["values"]=['南北走向','东西走向','西南-东北走向','东南西北走向']
        ComboBox_19.current(0)
        Fun.AddUserData(uiName,'ComboBox_19','南北走向','string','',0)
        Fun.AddUserData(uiName,'ComboBox_19','东西走向','string','0',0)
        Fun.AddUserData(uiName,'ComboBox_19','东南-西北走向','string','0',0)
        Fun.AddUserData(uiName,'ComboBox_19','西南-东北走向','string','0',0)
        ComboBox_19.bind("<<ComboboxSelected>>",Fun.EventFunction_Adaptor(xuanzhi_cmd.ComboBox_19_onSelect,uiName=uiName,widgetName="ComboBox_19"))
        Label_14 = tkinter.Label(Form_1,text="距离农田最小距离",width = 10,height = 4)
        Fun.Register(uiName,'Label_14',Label_14)
        Fun.SetControlPlace(uiName,'Label_14',74,190,100,20)
        Label_14.configure(relief = "flat")
        Entry_15_Variable = Fun.AddTKVariable(uiName,'Entry_15','')
        Entry_15 = tkinter.Entry(Form_1,textvariable=Entry_15_Variable)
        Fun.Register(uiName,'Entry_15',Entry_15)
        Fun.SetControlPlace(uiName,'Entry_15',224,204,120,20)
        Entry_15.configure(relief = "sunken")
        Label_12 = tkinter.Label(Form_1,text="距离建成区最小距离",width = 10,height = 4)
        Fun.Register(uiName,'Label_12',Label_12)
        Fun.SetControlPlace(uiName,'Label_12',65,152,114,20)
        Label_12.configure(relief = "flat")
        Button_20 = tkinter.Button(Form_1,text="开始选址程序",width = 10,height = 4)
        Fun.Register(uiName,'Button_20',Button_20)
        Fun.SetControlPlace(uiName,'Button_20',173,536,125,47)
        Button_20.configure(command=lambda:xuanzhi_cmd.Button_20_onCommand(uiName,"Button_20"))
        Label_21 = tkinter.Label(Form_1,text="建成区（shpfile）",width = 10,height = 4)
        Fun.Register(uiName,'Label_21',Label_21)
        Fun.SetControlPlace(uiName,'Label_21',47,51,148,20)
        Label_21.configure(relief = "flat")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = xuanzhi(root)
    root.mainloop()
