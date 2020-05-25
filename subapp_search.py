from tkinter import *
import sqlite3 as sql

#Search record Window
class Search:
	#Update record Function
	def update(rollno, name, year, program):
		db = sql.connect("students.db")
		c = db.cursor()
		print(rollno)
		#rno = rollno
		c.execute("UPDATE students SET Rollno=:rollno, Name=:name, Class=:year, Program=:program WHERE Rollno=:rollno" , {"rollno":rollno, "name":name,  "year":year, "program":program})
		db.commit()
		db.close()
	#Delete record Function
	def delete(rollno):
		db = sql.connect("students.db")
		c = db.cursor()
		c.execute("DELETE FROM students WHERE Rollno=(?)" , [rollno])
		db.commit()
		db.close()
	"""
	Search record Function
	Gets the Rollno from the user input and querys the database and 
	displays the corresponding information
	
	"""
	def search(rollno):
		root = Tk()
		root.config(bg = "#ffffff")
		frame = LabelFrame(root, bd = 4, bg = "#0f2c64")
		frame.grid(padx = 20, pady = 15)
		for widget in frame.winfo_children():
			widget.destroy()
		root.title("Edit record")
		db = sql.connect("students.db")
		c = db.cursor()
		print(rollno)
		rno = rollno
		c.execute("SELECT * FROM students WHERE Rollno=(?)" , [rno])
		stu_data = c.fetchall()
		student = []
		for element in stu_data:
			for data in element:
				student.append(data)
		print(student)
		Label(frame, text = "Student details:", bg = "royalblue4", fg = "grey85").grid(row = 0, padx = 100, pady = 20, columnspan = 2)
		Label(frame, text = "Roll No:", bg = "royalblue4", fg = "grey85").grid(row = 1, column = 0, padx = (50, 10))
		rollno = Entry(frame, width = 15)
		rollno.insert(END, student[0])
		rollno.grid(row = 1, column = 1, padx = (0, 90), pady = 10)
		Label(frame, text = "Name:", bg = "royalblue4", fg = "grey85").grid(row = 2, column = 0, padx = (50, 10))
		name = Entry(frame, width = 15)
		name.insert(END, student[1])
		name.grid(row = 2, column = 1, padx = (0, 90), pady = 10)
		Label(frame, text = "Class:", bg = "royalblue4", fg = "grey85").grid(row = 3, column = 0, padx = (50, 10))
		year = Entry(frame, width = 15)
		year.insert(END, student[2])
		year.grid(row = 3, column = 1, padx = (0, 90), pady = 10)
		Label(frame, text = "Program:", bg = "royalblue4", fg = "grey85").grid(row = 4, column = 0, padx = (50, 10))
		program = Entry(frame, width = 15)
		program.insert(END, student[3])
		program.grid(row = 4, column = 1, padx = (0, 90), pady = 10)
		Button(frame, text = "Update", background = "light blue", command = lambda:[Search.update(rollno.get(), name.get(), year.get(), program.get()), rollno.delete(0, END), name.delete(0, END), year.delete(0, END), program.delete(0, END)]).grid(row = 5, column = 0, padx = (90, 0), pady = 10)
		Button(frame, text = "Delete", background = "light blue", command = lambda:[Search.delete(rollno.get()), rollno.delete(0, END), name.delete(0, END), year.delete(0, END), program.delete(0, END)]).grid(row = 5, column = 1, padx = (0, 90), pady = 10)
		db.commit()
		db.close()
	#Search Function User Interface
	def search_button():
		root = Tk()
		root.config(bg = "#ffffff")
		frame = LabelFrame(root, bd = 4)
		frame.config(bg = "#0f2c64")
		frame.grid(padx = 20, pady = 15)
		root.title("Find a record")
		Label(frame, text = "Enter Student details:", bg = "royalblue4", fg = "grey85").grid(row = 0, padx = 100, pady = 20, columnspan = 2)
		Label(frame, text = "Roll No:", bg = "royalblue4", fg = "grey85").grid(row = 1, column = 0, padx = (50, 10))
		rollno = Entry(frame, width = 15)
		rollno.grid(row = 1, column = 1, padx = (0, 90), pady = 10)
		Button(frame, text = "Search", background = "light blue", command = lambda: [Search.search(rollno.get()), rollno.delete(0, END), root.destroy()]).grid(row = 5, column = 1, padx = (0, 90), pady = 10)	
		root.mainloop()
