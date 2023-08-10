from tkinter import *

root= Tk() 
root.geometry("300x320")  
root.resizable(0,0)  
root.title("Calculator")

def click(num):
    global i
    i = i + str(num)
    input_text.set(i)

def clear(): 
    global i 
    i = "" 
    input_text.set("")
    
def equal():
    global i
    ans = str(eval(i))
    input_text.set(ans)
    i = ""
 
i = "" 
input_text = StringVar()

frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
frame.pack(side=TOP)

entry = Entry(frame, font=('helvetica', 15, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
entry.grid(row=0, column=0)
entry.pack(ipady=10)

btn_frame = Frame(root, width=312, height=272.5, bg="grey")
btn_frame.pack()

clear = Button(btn_frame, text = "AC", width = 32, height = 3, bd = 0,fg="#fff",bg = "#ff9742", cursor = "hand2", command = lambda: clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btn_frame, text = "/", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

seven = Button(btn_frame, text = "7", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btn_frame, text = "8", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btn_frame, text = "9", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btn_frame, text = "*", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
four = Button(btn_frame, text = "4", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btn_frame, text = "5", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(5)).grid(row = 2, column = 1, padx = 1, pady = 1) 
six = Button(btn_frame, text = "6", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(6)).grid(row = 2, column = 2, padx = 1, pady = 1) 
minus = Button(btn_frame, text = "-", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
one = Button(btn_frame, text = "1", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(1)).grid(row = 3, column = 0, padx = 1, pady = 1) 
two = Button(btn_frame, text = "2", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(2)).grid(row = 3, column = 1, padx = 1, pady = 1) 
three = Button(btn_frame, text = "3", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(3)).grid(row = 3, column = 2, padx = 1, pady = 1) 
plus = Button(btn_frame, text = "+", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
zero = Button(btn_frame, text = "0", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btn_frame, text = ".", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btn_frame, text = "=", width = 10, height = 3, bd = 0, bg = "#a9a9a9" ,fg="#fff", cursor = "hand2", command = lambda: equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
root.mainloop()
