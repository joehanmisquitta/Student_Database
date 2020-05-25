from tkinter import *
import sqlite3 as sql
import hashlib
#login database interface used to register the user
class Signup():
	def signup(username, firstname, lastname, email, password):
		empty = [""]
		if username in empty:
			root = Tk()
			root.title("Invalid username")	
			Label(root, text = "Username connot be Empty").grid()
		elif firstname in empty:
			root = Tk()
			root.title("Invalid Firstname")	
			Label(root, text = "First name connot be Empty").grid()
		elif lastname in empty:
			root = Tk()
			root.title("Invalid Lastname")	
			Label(root, text = "Last name connot be Empty").grid()
		elif email in empty:
			root = Tk()
			root.title("Invalid Email")	
			Label(root, text = "Email connot be Empty").grid()
		elif password in empty:
			root = Tk()
			root.title("Invalid Password")	
			Label(root, text = "Password connot be Empty").grid()
		else:
			print("signup")
			db = sql.connect("Login.db")
			c = db.cursor()
			hashed_password= hashlib.md5(password.encode('utf-8')).hexdigest()
			c.execute("INSERT INTO users VALUES ( ?, ?, ?, ? , ?)", (username, firstname, lastname, email, hashed_password))
			# commit our command
			db.commit()
			#Close our connection
			db.close()

