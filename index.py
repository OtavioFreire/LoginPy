from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import DataBaser

janela = Tk() 
janela.title("RHpy")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width= False, height= False)
janela.attributes("-alpha", 0.95)
janela.iconbitmap(r'C:\Users\SrOta\Documents\Projetos\LoginPY\icons\userICO.ico')

#========= IMAGENS ============

photoUser = PhotoImage(file=r'C:\Users\SrOta\Documents\Projetos\LoginPY\icons\userR.png')

#========= WIDGETS ============
LeftFrame = Frame(janela, width=200,height=300, background="#3771a1", relief="raise")
LeftFrame.pack(side = LEFT)

RightFrame = Frame(janela, width=395, height=300, background="#ffd242", relief="raise")
RightFrame.pack(side = RIGHT)

LogoLabel = Label(LeftFrame, image = photoUser, bg="#3771a1")
LogoLabel.place(x = 25, y = 75)

UserLabel = Label(RightFrame, text="Username: ", font=("Century Gothic", 20), bg="#ffd242", fg="black")
UserLabel.place(x = 5, y = 90)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x = 150, y = 100)

PassLabel = Label(RightFrame, text="Password: ", font=("Century Gothic", 20), bg="#ffd242", fg="black")
PassLabel.place(x = 5, y = 130)

PassEntry = ttk.Entry(RightFrame, width=30, show = "*")
PassEntry.place(x = 150, y = 140)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Passwords = ?)
    """, (User, Pass))
    print("Logado")
    VeriFyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VeriFyLogin and Pass in VeriFyLogin):
            messagebox.showinfo(title = "Login Info", message="Acesso Confirmado. Bem vindo!")
    except TypeError:
            messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se está cadastrado no sistema!")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x = 115, y = 200 )

def Register():
    # Removendo Widgets de Login
    LoginButton.place(x = 5000, y = 5000)
    RegisterButton.place(x = 5000, y = 5000)
    #Inserindo Widgets de cadastro
    NomeLabel = Label(RightFrame, text="Nome: ", font=("Century Gothic", 20),bg="#ffd242", fg="black")
    NomeLabel.place(x = 5 , y = 5)
    
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x = 150, y = 15)
    
    EmailLabel = Label(RightFrame, text="E-Mail", font=("Century Gothic", 20), bg="#ffd242", fg="black")
    EmailLabel.place(x = 5, y = 45)
    
    EmailEntry = ttk.Entry(RightFrame, width = 30)
    EmailEntry.place(x = 150, y = 55)
    
    def RegisterInDB():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if (Name == "" and Email == "" and User == "" and Pass == ""): 
            messagebox.showerror(title = "Register Error", message="Não Deixe nenhum Campo Vazio. Preencha todos os campos")
        else:
            DataBaser.cursor.execute("""
                INSERT INTO Users(Names, Email, User, Passwords) VALUES(?, ?, ?, ?)
                """, (Name, Email, User, Pass))
            DataBaser.connection.commit()
            messagebox.showinfo(title="Register Info", message="Register Sucessfull")
    
    Register = ttk.Button(RightFrame, text="Register", width = 30, command=RegisterInDB)
    Register.place(x = 115, y = 200 )
    
    def BackToLogin():
        #Voltar aos menu anterior
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailEntry.place(x = 5000)
        EmailLabel.place(x = 5000)
        Register.place(x = 5000)
        Back.place(x = 5000)
        #Retornando botões Login e Senha
        LoginButton.place(x = 115, y = 200 )
        RegisterButton.place(x = 145, y = 230 ) 
    
    Back = ttk.Button(RightFrame, text="Back", width = 20, command= BackToLogin)
    Back.place(x = 145, y = 230)   
    
RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command= Register)
RegisterButton.place(x = 145, y = 230 ) 

janela.mainloop()