from tkinter import *
import tkinter.font as tkFont
import sys

#filepath variables
file1 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn1.txt"
file2 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn2.txt"
file3 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn3.txt"
file4 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn4.txt"
file5 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn5.txt"
file6 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn6.txt"
file7 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn7.txt"
file8 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn8.txt"
file9 = "/Users/martm/Desktop/CIS293/Project4/CIS293_BrainDump-master/CIS293_BrainDump-master/btn_db/btn9.txt"

#Creates pop-up window for To Do
class popupWindow(object):
    def __init__(self,master, file):
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        top=self.top=Toplevel(master)
        top.geometry("300x325")
        #self.top.bind_class('popupWindow', "<Return>", self.cleanup)
        self.l=Label(top,text="To Do:", font=self.fontStyle)
        self.l.pack()
        self.e=Text(top, height="15", width="30")
        self.e.insert(END, self.readToDo(file))
        self.e.pack()
        self.e.focus()

        # Bind enter key to accept text; same as clicking ok button
        self.e.bind("<Return>", self.onReturn)
        # Bind shift+enter for line break
        self.e.bind("<Shift-Return>", self.onShiftReturn)

        self.space=Label(top, text="")
        self.space.pack()
        self.b=Button(top,text='Ok', pady="10", height="1", width="15", command=self.cleanup)
        self.b.pack()
        self.space2=Label(top, text="")
        self.space2.pack()
    
    def cleanup(self):
        self.value=self.e.get("1.0",'end-1c')
        self.top.destroy()
        print(self.value)
    
    def readToDo(self, file):
        with open(file, "r") as f:
            return (f.read())

    # function when enter is pressed
    def onReturn(self, arg):
        self.value=self.e.get("1.0",'end-1c')
        self.top.destroy()
        print(self.value)

    # function when shift+enter is pressed
    def onShiftReturn(self, arg):
        "\n"


# --------------------------------------------------------------------------------

# Creates main window
class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.master.title("Brain Dump")

        self.button1_text = StringVar()
        self.button1_text.set(self.readFile(file1))
        self.button1=Button(master, width=20, height=10, wraplength=170, textvariable=self.button1_text, command=self.addToDo1)
        self.button1.grid(row=0, column=0)
        self.button2_text = StringVar()
        self.button2_text.set(self.readFile(file2))
        self.button2=Button(master, width=20, height=10, wraplength=170, textvariable=self.button2_text, command=self.addToDo2)
        self.button2.grid(row=0, column=1)
        self.button3_text = StringVar()
        self.button3_text.set(self.readFile(file3))
        self.button3=Button(master, width=20, height=10, wraplength=170, textvariable=self.button3_text, command=self.addToDo3)
        self.button3.grid(row=0, column=2)
        
        self.button4_text = StringVar()
        self.button4_text.set(self.readFile(file4))
        self.button4=Button(master, width=20, height=10, wraplength=170, textvariable=self.button4_text, command=self.addToDo4)
        self.button4.grid(row=1, column=0)
        self.button5_text = StringVar()
        self.button5_text.set(self.readFile(file5))
        self.button5=Button(master, width=20, height=10, wraplength=170, textvariable=self.button5_text, command=self.addToDo5)
        self.button5.grid(row=1, column=1)
        self.button6_text = StringVar()
        self.button6_text.set(self.readFile(file6))
        self.button6=Button(master, width=20, height=10, wraplength=170, textvariable=self.button6_text, command=self.addToDo6)
        self.button6.grid(row=1, column=2)

        self.button7_text = StringVar()
        self.button7_text.set(self.readFile(file7))
        self.button7=Button(master, width=20, height=10, wraplength=170, textvariable=self.button7_text, command=self.addToDo7)
        self.button7.grid(row=2, column=0)
        self.button8_text = StringVar()
        self.button8_text.set(self.readFile(file8))
        self.button8=Button(master, width=20, height=10, wraplength=170, textvariable=self.button8_text, command=self.addToDo8)
        self.button8.grid(row=2, column=1)
        self.button9_text = StringVar()
        self.button9_text.set(self.readFile(file9))
        self.button9=Button(master, width=20, height=10, wraplength=170, textvariable=self.button9_text, command=self.addToDo9)
        self.button9.grid(row=2, column=2)
        
    def popup(self, file):
        self.w=popupWindow(self.master, file)
        self.master.wait_window(self.w.top)
    
    def readFile(self,file):
        with open(file, "r") as f:
            return (f.read())

    def printFile(self,file):
        todo = open(file,'w')
        todo.write(self.w.value)

    def addToDo1(self):
        self.popup(file1)
        self.button1_text.set(self.w.value)
        self.printFile(file1)

    def addToDo2(self):
        self.popup(file2)
        self.button2_text.set(self.w.value)
        self.printFile(file2)
    
    def addToDo3(self):
        self.popup(file3)
        self.button3_text.set(self.w.value)
        self.printFile(file3)

    def addToDo4(self):
        self.popup(file4)
        self.button4_text.set(self.w.value)
        self.printFile(file4)

    def addToDo5(self):
        self.popup(file5)
        self.button5_text.set(self.w.value)
        self.printFile(file5)

    def addToDo6(self):
        self.popup(file6)
        self.button6_text.set(self.w.value)
        self.printFile(file6)

    def addToDo7(self):
        self.popup(file7)
        self.button7_text.set(self.w.value)
        self.printFile(file7)

    def addToDo8(self):
        self.popup(file8)
        self.button8_text.set(self.w.value)
        self.printFile(file8)

    def addToDo9(self):
        self.popup(file9)
        self.button9_text.set(self.w.value)
        self.printFile(file9)

# App constructor
if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
