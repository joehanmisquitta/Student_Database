from tkinter import *
import sqlite3 as sql
import hashlib
from subapp import app
#login database interface used to authenticate the user
class Login():
	def login(email_gui, password_gui):
		db = sql.connect("Login.db")
		c = db.cursor()
		c.execute(" SELECT * FROM users WHERE email = (?)", [email_gui])
		users = c.fetchall()
		print(users)
		username = []
		name = []
		email = []
		password = []
		for user in users:
			username.append(user[0])
			name.append(user[1]+" "+user[2])
			email.append(user[3])
			password.append(user[4])
						
		e_mail = email_gui
		if e_mail in email:
			index = email.index(e_mail)
			passwd = password[index]
			passwrd = hashlib.md5(password_gui.encode('utf-8')).hexdigest()
			if str(passwrd) in passwd:
				name = name[index]
				username = username[index]
				app(name, username)
			else:
				#incorrect_password()
				root = Tk()
				root.title("Incorrect Password")
				Label(root, text = "The given Password is incorrect or doesn't exist").grid()
		else:
		#	incorrect_email()
			root = Tk()
			root.title("Incorrect Email")	
			Label(root, text = "The given E-Mail Address incorrect or doesn't exist").grid()
		
		# commit our command
		db.commit()
		#Close our connection
		db.close()

		