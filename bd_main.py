from tkinter import *
import tkinter.font as tkFont
import sys
file1 = "btn_db/btn1.txt"
file2 = "btn_db/btn2.txt"
file3 = "btn_db/btn3.txt"
file4 = "btn_db/btn4.txt"
file5 = "btn_db/btn5.txt"
file6 = "btn_db/btn6.txt"
file7 = "btn_db/btn7.txt"
file8 = "btn_db/btn8.txt"
file9 = "btn_db/btn9.txt"

#Creates pop-up window for To Do
class popupWindow(object):
    def __init__(self,master, file):
        #set window and frames
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        top=self.top=Toplevel(master)
        top.geometry("300x325")
        topFrame = Frame(top)
        topFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack()
        #top frame with todo label and textbox
        self.l=Label(topFrame,text="To Do:", font=self.fontStyle)
        self.l.pack()
        self.e=Text(topFrame, height="15", width="30")
        self.e.insert(END, self.readToDo(file))
        self.e.pack()
        self.e.focus()
        
        #bottom frame with ok and clear buttons
        self.space=Label(bottomFrame, text="")
        self.space.pack()
        self.b=Button(bottomFrame,text='Ok', pady="10", height="1", width="10", command=self.enter)
        self.b.pack(side=LEFT)
        self.c=Button(bottomFrame, text='Clear', pady="10", height="1", width="10", command=self.clear)
        self.c.pack(side=LEFT)
        self.space2=Label(top, text="")
        self.space2.pack()

        # Bind enter key to accept text; same as clicking ok button
        self.e.bind("<Return>", self.onReturn)
        # Bind shift+enter for line break
        self.e.bind("<Shift-Return>", self.onShiftReturn)

    #gets textbox value
    def enter(self):
        self.value=self.e.get("1.0",'end-1c')
        self.top.destroy()
        print(self.value)
    
    #clears textbox value
    def clear(self):
        self.e.delete('1.0', 'end-1c')
        self.e.insert('end-1c', "")
        self.enter()

    #reads text file to display in textbox
    def readToDo(self, file):
        with open(file, "r") as f:
            return (f.read())

    # function when enter is pressed
    def onReturn(self, arg):
        self.enter()

    # function when shift+enter is pressed
    def onShiftReturn(self, arg):
        "\n"

# --------------------------------------------------------------------------------

# Creates main window
class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.master.title("Brain Dump")
        
        #button setup
        self.button1_text = StringVar()
        self.button1_text.set(self.readFile(file1))
        self.button1=Button(master, width=20, height=10, wraplength=170, textvariable=self.button1_text, command= lambda: self.addToDo(file1, 1))
        self.button1.grid(row=0, column=0)

        self.button2_text = StringVar()
        self.button2_text.set(self.readFile(file2))
        self.button2=Button(master, width=20, height=10, wraplength=170, textvariable=self.button2_text, command=lambda: self.addToDo(file2, 2))
        self.button2.grid(row=0, column=1)

        self.button3_text = StringVar()
        self.button3_text.set(self.readFile(file3))
        self.button3=Button(master, width=20, height=10, wraplength=170, textvariable=self.button3_text, command=lambda: self.addToDo(file3, 3))
        self.button3.grid(row=0, column=2)
        
        self.button4_text = StringVar()
        self.button4_text.set(self.readFile(file4))
        self.button4=Button(master, width=20, height=10, wraplength=170, textvariable=self.button4_text, command=lambda: self.addToDo(file4, 4))
        self.button4.grid(row=1, column=0)

        self.button5_text = StringVar()
        self.button5_text.set(self.readFile(file5))
        self.button5=Button(master, width=20, height=10, wraplength=170, textvariable=self.button5_text, command=lambda: self.addToDo(file5, 5))
        self.button5.grid(row=1, column=1)

        self.button6_text = StringVar()
        self.button6_text.set(self.readFile(file6))
        self.button6=Button(master, width=20, height=10, wraplength=170, textvariable=self.button6_text, command=lambda: self.addToDo(file6, 6))
        self.button6.grid(row=1, column=2)

        self.button7_text = StringVar()
        self.button7_text.set(self.readFile(file7))
        self.button7=Button(master, width=20, height=10, wraplength=170, textvariable=self.button7_text, command=lambda: self.addToDo(file7, 7))
        self.button7.grid(row=2, column=0)

        self.button8_text = StringVar()
        self.button8_text.set(self.readFile(file8))
        self.button8=Button(master, width=20, height=10, wraplength=170, textvariable=self.button8_text, command=lambda: self.addToDo(file8, 8))
        self.button8.grid(row=2, column=1)

        self.button9_text = StringVar()
        self.button9_text.set(self.readFile(file9))
        self.button9=Button(master, width=20, height=10, wraplength=170, textvariable=self.button9_text, command=lambda: self.addToDo(file9, 9))
        self.button9.grid(row=2, column=2)
    
    #creates popup window
    def popup(self, file):
        self.w=popupWindow(self.master, file)
        self.master.wait_window(self.w.top)
    
    #opens text file and displays text data
    def readFile(self,file):
        with open(file, "r") as f:
            return (f.read())

    #writes to do to text file
    def printFile(self,file):
        todo = open(file,'w')
        todo.write(self.w.value)

    #consolidated todo function - accepts filename and button number as parameters
    def addToDo (self, filename, buttonname):
        self.popup(filename)
        self.button = self.getButton((buttonname))
        self.button.set(self.w.value)
        self.printFile(filename)
    
    #switch function that determines button's name
    def getButton(self, button):
        switcher = {
            1: self.button1_text,
            2: self.button2_text,
            3: self.button3_text,
            4: self.button4_text,
            5: self.button5_text,
            6: self.button6_text,
            7: self.button7_text,
            8: self.button8_text,
            9: self.button9_text
        }
        return switcher.get(button, "invalid")

# App constructor
if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
