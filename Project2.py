#coding=utf-8
#import libs 
import sys
import Project2_cmd
import Project2_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Project2:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Project2_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,640,480)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 640,height = 480)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="选址选线小程序",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Fun.SetControlPlace(uiName,'Label_2',90,57,454,68)
        Label_2.configure(fg = "#0000ff")
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='System', size=45,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Button_3 = tkinter.Button(Form_1,text="选址",width = 10,height = 4)
        Fun.Register(uiName,'Button_3',Button_3)
        Fun.SetControlPlace(uiName,'Button_3',243,206,150,49)
        Button_3.configure(command=lambda:Project2_cmd.Button_3_onCommand(uiName,"Button_3"))
        Button_3_Ft=tkinter.font.Font(family='System', size=24,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_3.configure(font = Button_3_Ft)
        Button_4 = tkinter.Button(Form_1,text="选线",width = 10,height = 4)
        Fun.Register(uiName,'Button_4',Button_4)
        Fun.SetControlPlace(uiName,'Button_4',243,304,150,57)
        Button_4.configure(command=lambda:Project2_cmd.Button_4_onCommand(uiName,"Button_4"))
        Button_4_Ft=tkinter.font.Font(family='System', size=24,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_4.configure(font = Button_4_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Project2(root)
    root.mainloop()
