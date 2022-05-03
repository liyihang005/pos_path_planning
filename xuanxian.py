#coding=utf-8
#import libs 
import sys
import xuanxian_cmd
import xuanxian_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  xuanxian:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = xuanxian_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,480,621)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 480,height = 621)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="限制条件",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Fun.SetControlPlace(uiName,'Label_2',45,17,188,53)
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='System', size=20,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_3 = tkinter.Label(Form_1,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_3',Label_3)
        Fun.SetControlPlace(uiName,'Label_3',41,75,100,20)
        Label_3.configure(relief = "flat")
        Entry_4_Variable = Fun.AddTKVariable(uiName,'Entry_4','')
        Entry_4 = tkinter.Entry(Form_1,textvariable=Entry_4_Variable)
        Fun.Register(uiName,'Entry_4',Entry_4)
        Fun.SetControlPlace(uiName,'Entry_4',197,77,120,20)
        Entry_4.configure(relief = "sunken")
        Label_5 = tkinter.Label(Form_1,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_5',Label_5)
        Fun.SetControlPlace(uiName,'Label_5',41,129,100,20)
        Label_5.configure(relief = "flat")
        Entry_6_Variable = Fun.AddTKVariable(uiName,'Entry_6','')
        Entry_6 = tkinter.Entry(Form_1,textvariable=Entry_6_Variable)
        Fun.Register(uiName,'Entry_6',Entry_6)
        Fun.SetControlPlace(uiName,'Entry_6',198,133,120,20)
        Entry_6.configure(relief = "sunken")
        Label_7 = tkinter.Label(Form_1,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_7',Label_7)
        Fun.SetControlPlace(uiName,'Label_7',41,194,100,20)
        Label_7.configure(relief = "flat")
        Entry_8_Variable = Fun.AddTKVariable(uiName,'Entry_8','')
        Entry_8 = tkinter.Entry(Form_1,textvariable=Entry_8_Variable)
        Fun.Register(uiName,'Entry_8',Entry_8)
        Fun.SetControlPlace(uiName,'Entry_8',196,195,120,20)
        Entry_8.configure(relief = "sunken")
        Label_9 = tkinter.Label(Form_1,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_9',Label_9)
        Fun.SetControlPlace(uiName,'Label_9',41,264,100,20)
        Label_9.configure(relief = "flat")
        Entry_10_Variable = Fun.AddTKVariable(uiName,'Entry_10','')
        Entry_10 = tkinter.Entry(Form_1,textvariable=Entry_10_Variable)
        Fun.Register(uiName,'Entry_10',Entry_10)
        Fun.SetControlPlace(uiName,'Entry_10',197,266,120,20)
        Entry_10.configure(relief = "sunken")
        Label_11 = tkinter.Label(Form_1,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_11',Label_11)
        Fun.SetControlPlace(uiName,'Label_11',41,333,100,20)
        Label_11.configure(relief = "flat")
        Entry_12_Variable = Fun.AddTKVariable(uiName,'Entry_12','')
        Entry_12 = tkinter.Entry(Form_1,textvariable=Entry_12_Variable)
        Fun.Register(uiName,'Entry_12',Entry_12)
        Fun.SetControlPlace(uiName,'Entry_12',197,331,120,20)
        Entry_12.configure(relief = "sunken")
        Label_13 = tkinter.Label(Form_1,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_13',Label_13)
        Fun.SetControlPlace(uiName,'Label_13',48,411,100,20)
        Label_13.configure(relief = "flat")
        Entry_14_Variable = Fun.AddTKVariable(uiName,'Entry_14','')
        Entry_14 = tkinter.Entry(Form_1,textvariable=Entry_14_Variable)
        Fun.Register(uiName,'Entry_14',Entry_14)
        Fun.SetControlPlace(uiName,'Entry_14',195,412,120,20)
        Entry_14.configure(relief = "sunken")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = xuanxian(root)
    root.mainloop()
