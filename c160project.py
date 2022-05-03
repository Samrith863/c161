from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os
root=Tk()
root.title("NotePad")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="yellow")

label1=Label(root,text="File Name")
input_1=Entry(root)
text_area=Text(root,height=35,width=80)

name=""
def openFile():
    global name
    text_area.delete(1.0,END)
    input_1.delete(0,END)
    file_path=filedialog.askopenfilename(title="Open Files",filetypes=(("text files","*.txt"),))
    print(file_path)
    file_basename=os.path.basename(file_path)
    print(file_basename)
    file_format=file_basename.split('.')[0]
    input_1.insert(END,file_format)
    root.title(file_format)
    text_file=open(file_basename,'r')
    paragraph=text_file.read()
    text_area.insert(END,paragraph)
    text_file.close()
    
    
                                         
open_btn=Button(root,text="Open",command=openFile)



open_btn.place(relx=0.11,rely=0.03,anchor=CENTER)

label1.place(relx=0.28,rely=0.03,anchor=CENTER)
input_1.place(relx=0.46,rely=0.03,anchor=CENTER)
text_area.place(relx=0.5,rely=0.55,anchor=CENTER)
root.mainloop()

