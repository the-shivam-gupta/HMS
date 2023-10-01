import tkinter
from window2 import menu

#variables
root=()
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
#command for login button
def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='shivam' and S2=='123'):
        menu()
    elif(S1=='sunny' and S2=='456'):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n PLEASE TRY AGAIN",fg="red",font='Times 36  italic')
        error.pack()


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("1550x900")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="Hospital Management System",bg='light blue',fg='blue',font='Times 56 bold italic')
    username=tkinter.Label(topframe,text="USERNAME",font="arial 36 bold" )
    userbox = tkinter.Entry(topframe,font="arial 36 bold")
    password=tkinter.Label(bottomframe,text="PASSWORD",font="arial 36 bold")
    passbox = tkinter.Entry(bottomframe,show="*",font="arial 36 bold")
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET,font="arial 38 bold",fg='red')
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("WELCOME to HMS!! **Please Login**") 
    root.mainloop()

Entry()

