from tkinter import *
from tkinter import font
from tkinter import ttk

janela = Tk() 
janela.title("RHpy")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width= False, height= False)
janela.attributes("-alpha", 0.95)

#========= IMAGENS ============

photoUser = PhotoImage(file="icons/userR.png")

#========= WIDGETS ============
LeftFrame = Frame(janela, width=200,height=300, background="#3771a1", relief="raise")
LeftFrame.pack(side = LEFT)

RightFrame = Frame(janela, width=395, height=300, background="#ffd242", relief="raise")
RightFrame.pack(side = RIGHT)

LogoLabel = Label(LeftFrame, image = photoUser, bg="#3771a1")
LogoLabel.place(x = 25, y = 75)

UserLabel = Label(RightFrame, text="Username: ", font=("Century Gothic", 20), bg="#ffd242", fg="black")
UserLabel.place(x = 5, y = 80)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x = 150, y = 90)

PassLabel = Label(RightFrame, text="Password: ", font=("Century Gothic", 20), bg="#ffd242", fg="black")
PassLabel.place(x = 5, y = 120)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x = 150, y = 130)

LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x = 115, y = 200 )

RegisterButton = ttk.Button(RightFrame, text="Register", width=20)
RegisterButton.place(x = 145, y = 230 ) 

janela.mainloop()