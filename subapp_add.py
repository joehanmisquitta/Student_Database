from tkinter import *
import sqlite3 as sql

#Add record Window
class Add:
	#Add records to the interface from the user input
	def add(rollno, name, year, program):
		db = sql.connect("students.db")
		c = db.cursor()
		c.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (rollno, name, year, program))
		db.commit()
		db.close()
	#Add record UI
	def add_button():
		root = Tk()
		root.config(bg = "#ffffff")
		root.title("Add a record")
		frame = LabelFrame(root, bd = 4).grid(padx = 20, pady = 15)
		Label(frame, text = "Enter Student details:", bg = "white").grid(row = 0, padx = 100, pady = 20, columnspan = 2)
		Label(frame, text = "Roll No:", bg = "white").grid(row = 1, column = 0, padx = (50, 10))
		rollno = Entry(frame, width = 15)
		rollno.grid(row = 1, column = 1, padx = (0, 90), pady = 10)
		Label(frame, text = "Name:", bg = "white").grid(row = 2, column = 0, padx = (50, 10))
		name = Entry(frame, width = 15)
		name.grid(row = 2, column = 1, padx = (0, 90), pady = 10)
		Label(frame, text = "Class:", bg = "white").grid(row = 3, column = 0, padx = (50, 10))
		year = Entry(frame, width = 15)
		year.grid(row = 3, column = 1, padx = (0, 90), pady = 10)
		Label(frame, text = "Program:", bg = "white").grid(row = 4, column = 0, padx = (50, 10))
		program = Entry(frame, width = 15)
		program.grid(row = 4, column = 1, padx = (0, 90), pady = 10)
		Button(frame, text = "Add", background = "light blue", command = lambda:[Add.add(rollno.get(), name.get(), year.get(), program.get()), rollno.delete(0, END), name.delete(0, END), year.delete(0, END), program.delete(0, END)]).grid(row = 5, column = 1, padx = (0, 90), pady = 10)
	
