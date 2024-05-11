from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter+password_number+password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    pwd_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website  = web_input.get()
    try:
        with open("password.json","r") as file:
            data_file = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops",message="Data does not exist")
    else:            
        if website in data_file:
            email = data_file[website]["Email"]
            password = data_file[website]["Password"]
            messagebox.showinfo(title="Required data",message=f"Email : {email}\n Password : {password}")
        else:
            messagebox.showerror(title="error",message=f"No details for {website} exists")    
    
    
    





# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website  = web_input.get()
    email = email_input.get()
    password = pwd_input.get()
    new_data = {
        website : {
            "Email":email,
            "Password" : password
        }
    }
    
    if website == "" or email=="" or password=="":
        messagebox.showinfo(title="Oops",message="Please don't leave any data")
    else:    
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered \n Website : {website}\n Email : {email}\n Password : {password}\n It is ok to save ?")
        if is_ok:
            try:
                with open("password.json","r") as file:
                    data = json.load(file) #read the old data
            except FileNotFoundError:
                with open("password.json","w") as file:    
                    json.dump(new_data,file,indent=4)
            else:            
                data.update(new_data)  #update old data with new data 
                with open("password.json","w") as file:    
                    json.dump(data,file,indent=4)  #write the data
   
            finally:    
                file.close()
                web_input.delete(0,END) 
                pwd_input.delete(0,END)
            
                       
            
        


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
my_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=my_image)
canvas.grid(column=1,row=0)

web = Label(text="Website")
web.grid(column=0,row=1)

web_input = Entry(width=22)
web_input.focus()
web_input.grid(column=1,row=1)

search_btn = Button(width=10,text="search",command=find_password)
search_btn.grid(column=2,row=1)

email = Label(text="Email/Username")
email.grid(column=0,row=2)

email_input = Entry(width=35)
email_input.insert(0,"sneha@gmail.com")
email_input.grid(column=1,row=2,columnspan=2)

pwd = Label(text="Password")
pwd.grid(column=0,row=3)

pwd_input = Entry(width=22)
pwd_input.grid(column=1,row=3)

genbtn = Button(width=10,text="Generate",command=generate_pwd)
genbtn.grid(column=2,row=3)

addbtn =Button(width=30,text="Add",command= add_password)
addbtn.grid(column=1,row=4,columnspan=2)


screen.mainloop()