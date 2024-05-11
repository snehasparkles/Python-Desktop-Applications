from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageFont,Image,ImageTk,ImageDraw
import os

root =Tk()
root.configure(bg="#fadeff")
root.title("WATER MARKING APP")
root.geometry("735x470+100+100")
root.resizable(False,False)



def chooseimg():
    global filename
    filename = filedialog.askopenfilename(title="select image file",filetypes=(('PNG file','*.png'),
                                                                               ('JPG file','*.jpg'),
                                                                               ('ALL file','*.txt')))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img,width=570,height=270)
    lb1.image = img
    
def apply():
    if filename:
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
        draw.text((10,10),"water mark",fill="white",font=ImageFont.truetype("arial.ttf",20))
        img.show()
        # photo = ImageTk.PhotoImage(file=img)
        # lb1.configure(image=photo)
        # lb1.image = photo
        
    else:
        print("no image is selected")    

def download():
    if filename:
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
        draw.text((10,10),"water mark",fill="white",font=ImageFont.truetype("arial.ttf",20))
        imgsave = filedialog.asksaveasfilename(defaultextension=".png")
        img.save(imgsave)
       
        







#icon
icon = PhotoImage(file="icon.png")
root.iconphoto(False,icon)

frame = Frame(root,width=700,height=370,bg="#fadeff")
frame.place(x=50,y=50)

# logo = PhotoImage(file="logo.png")
# Label(root,image=logo,bg="#fff").place(x=10,y=10)
Label(root,text="Add water marking in image",font="arial 20 bold",bg="#fadeff").place(x=150,y=20)


#select image
selectimage = Frame(frame,width=600,height=350,bg="#d6dee5")
selectimage.place(x=10,y=10)

f = Frame(selectimage,bd=3,bg="black",width=580,height=280,relief=GROOVE)
f.place(x=10,y=10)


lb1 = Label(f,bg="black")
lb1.place(x=0,y=0)


Button(selectimage,text="Select Image",width=10,height=1,font="arial 14 bold",command=chooseimg).place(x=10,y=300)
Button(selectimage,text="Apply mark",width=10,height=1,font="arial 14 bold",command=apply).place(x=165,y=300)
Button(selectimage,text="Download",width=10,height=1,font="arial 14 bold",command=download).place(x=320,y=300)
Button(selectimage,text="Cancel",width=9,height=1,font="arial 14 bold",command=root.quit).place(x=475,y=300)






root.mainloop()
