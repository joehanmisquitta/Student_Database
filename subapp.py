from tkinter import *
import sqlite3 as sql
from subapp_add import Add
from subapp_search import Search
#main app 
def app(name, username): 
	main = Tk()
	main.config(bg = "#ffffff")    
	student_frame = LabelFrame(main, bd = 5, bg = "#0f2c64")
	student_frame.grid(row = 1, pady = 10, padx = 20)
	student_frame1 = LabelFrame(main, bd = 5, bg = "#0f2c64")
	student_frame1.grid(row = 0)
	main.title("Student Database")
	db = sql.connect("students.db")
	c = db.cursor()
	student = []
	c.execute("SELECT * FROM students")
	students = c.fetchall()
	for element in students:
		student.append(element)	
	total_rows = len(student)
	total_columns = len(student[0])
	def table():
		for i in range(total_rows):
			for j in range(total_columns):
				e = Entry(student_frame, width=16, justify= 'center')
				e.grid(row=i, column=j) 
				e.insert(END, student[i][j])
	def refresh():
		main.destroy()
		student.clear()
		app(name, username)
	Label(student_frame1, text = "Hello "+name+" Your Username is "+username, relief = GROOVE, bg = "royalblue4", fg = "grey85").grid(row = 0, columnspan = 4, ipadx = 130)
	Button(student_frame1 , text = "Add", background = "light blue", command = Add.add_button).grid(row = 1, column = 0, ipadx = 120)
	Button(student_frame1 , text = "Search", background = "light blue", command = Search.search_button).grid(row = 1, column = 1, ipadx = 120)
	Button(student_frame1 , text = "Refresh", background = "light blue", command = refresh).grid(row = 1, column = 3, ipadx = 120)
	
	table()
	db.commit()
	db.close()

			