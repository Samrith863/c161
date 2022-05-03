from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("NotePad")
root.geometry("500x250")
root.configure(background="yellow")
label1=Label(root,text="File Name")
input_1=Entry(root)
text_area=Text(root,height=5,width=40)

def clearInput():
    input_1.delete(0,END)
def clearTextarea():
    text_area.delete(1.0,END)
def addToInput():
    input_1.insert(END,"NewFile")

input_clear_btn=Button(root,text="Clear Input Field",command=clearInput)
textarea_clear_btn=Button(root,text="Clear Text Area",command=clearTextarea)
add_btn=Button(root,text="Add Data To Input Field",command=addToInput)

input_clear_btn.place(relx=0.25,rely=0.7,anchor=CENTER)
textarea_clear_btn.place(relx=0.45,rely=0.7,anchor=CENTER)
add_btn.place(relx=0.7,rely=0.7,anchor=CENTER)
label1.place(relx=0.28,rely=0.1,anchor=CENTER)
input_1.place(relx=0.5,rely=0.1,anchor=CENTER)
text_area.place(relx=0.5,rely=0.55,anchor=CENTER)
root.mainloop()
