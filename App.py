from tkinter import *
import sqlite3 as sql
from login import Login
from signup import Signup

#frame management
def replace_login():
	for widget in frame.winfo_children():
		widget.destroy()  
	App.signup()		
def replace_signup():
	for widget in frame.winfo_children():
		widget.destroy()  
	App.login()		

class App():		
	def signup ():
		#GUI of The signup page
		root.title("Signup")
		Label(frame, text="Username:", bg = "royalblue4", fg = "grey85").grid(row = 0, column = 0)
		username = Entry(frame, width = 30)
		username.grid(row = 0, column = 1, padx = 20, pady =10)     
		Label(frame, text="First Name:", bg = "royalblue4", fg = "grey85").grid(row = 1, column = 0)
		firstname = Entry(frame, width = 30)
		firstname.grid(row = 1, column = 1, padx = 20, pady =10)     
		Label(frame, text="Last Name:", bg = "royalblue4", fg = "grey85").grid(row = 2, column = 0)
		lastname = Entry(frame, width = 30)
		lastname.grid(row = 2, column = 1, padx = 20, pady =10)     
		Label(frame, text="Email:", bg = "royalblue4", fg = "grey85").grid(row = 3, column = 0)
		email = Entry(frame, width = 30)
		email.grid(row = 3, column = 1, padx = 20, pady =10)     
		Label(frame, text="Password:", bg = "royalblue4", fg = "grey85").grid(row = 4, column = 0)
		password = Entry(frame, width = 30)
		password.grid(row = 4, column = 1, padx = 20, pady =10) 
		Button(frame, text = "Signup", background = "light blue", command = lambda: [Signup.signup(username.get(), firstname.get(), lastname.get(), email.get(), password.get()), username.delete(0, END), firstname.delete(0, END), lastname.delete(0, END), email.delete(0, END), password.delete(0, END)]).grid(row = 5, ipadx= 100, columnspan = 2)
		Button(frame, text = "Go Back to Login", background = "light blue", command = replace_signup).grid(row = 6, columnspan = 2, pady = 10)
		root.mainloop()
	def login ():
		#GUI of The login page
		root.title("Login")
		Label(frame, text="Email:", bg = "royalblue4", fg = "grey85").grid(row = 1, column = 0, padx = (20,0), ipadx = 40)
		email = Entry(frame, width = 30)
		email.grid(row = 1, column = 1, padx = 20, pady =10)     
		Label(frame, text="Password:", bg = "royalblue4", fg = "grey85").grid(row = 2, column = 0, padx = (20,0))
		password = Entry(frame, width = 30, show = "•")
		password.grid(row = 2, column = 1, padx = 20, pady =10)
		Button(frame, text = "Login", background = "light blue", command = lambda: [Login.login(email.get(), password.get()), email.delete(0, END), password.delete(0, END), root.destroy()]).grid(row = 3, columnspan = 2, ipadx = 60)
		Button(frame, text = "Signup", background = "light blue", command = replace_login).grid(row = 4 , columnspan = 2, pady = 10, ipadx = 48)
		root.mainloop()
#Main window 
root = Tk()
root.minsize(1400, 1200)
root.maxsize(1400, 1200)
root.config(bg = "#ffffff")
frame = LabelFrame(root, text = "Login", bd=5, fg = "white")
frame.config(bg = "#0f2c64")
frame.grid(padx=250, pady= 200)		
App.login()


