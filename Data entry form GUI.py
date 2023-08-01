import tkinter
from tkinter import ttk

def enter_data():
    print("USER INFORMATION :")
    #USER INFO
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()


    print("First name : ",firstname)
    print("Last name : ",lastname)
    print("Title : ",title)
    print("Age : ",age)
    print("Nationality : ",nationality)


window = tkinter.Tk()
window.title("Data entry form")

frame = tkinter.Frame(window)
frame.pack()

# Saving user info
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid( row=0 , column=0 , padx=20 , pady=20 )

#Assigning label
first_name_label = tkinter.Label(user_info_frame,text = "First name")
first_name_label.grid(row = 0,column=0)

last_name_label = tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row = 0 ,column = 1)

#creating entry
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1 , column = 0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row =1 ,column =1)

#to create dropdown
title_label = tkinter.Label(user_info_frame,text="Title")
title_combobox = ttk.Combobox(user_info_frame,values=[ "","Mr." , "Ms." , "Dr."])
title_label.grid(row = 0 , column = 2)
title_combobox.grid(row=1,column=2)

#to create spinbox for age
age_label = tkinter.Label(user_info_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame,from_ =18, to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

#to create another dropdown
nationality_label = tkinter.Label(user_info_frame,text="Nationality")
nationality_label.grid(row=2,column=1)
nationality_combobox =ttk.Combobox(user_info_frame,values=["IND","PAK","JAP"])
nationality_combobox.grid(row=3,column=1)

#To create spaces between widgets
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



#
#TO CREATE SECOND LABEL FRAME saving course info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)

#registered_label = tkinter.Label(courses_frame,text="Registration Status")
registered_label = tkinter.Label(courses_frame, text="Registration Status")

registered_check = tkinter.Checkbutton(courses_frame,text="Currently Registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

#TO CREATE COMPLETE COURSES DROPDOWN
completed_courses = tkinter.Label(courses_frame,text="Complete Courses")
completed_courses.grid(row=0,column=1)
completed_spinbox = ttk.Spinbox(courses_frame,from_ = 1, to=20)
completed_spinbox.grid(row=1,column=1)

#TO ADD SEMMISTERS
semister_label = tkinter.Label(courses_frame,text="Semisters")
semister_label.grid(row=0,column=3)
semister_spinbox = ttk.Spinbox(courses_frame,from_ = 0 ,to=8)
semister_spinbox.grid(row=1,column=3)

#TO ADD EVEN SPACING
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


#TO CREATE NEW LABEL FRAME
terms_label = tkinter.LabelFrame(frame,text="Terms & Conditions")
terms_label.grid(row=2,column=0,sticky="news",padx=20,pady=20)

#TO ADD CHECK BUTTON
iact_check = tkinter.Checkbutton(terms_label,text="I accept the terms and conditions.")
iact_check.grid(row=0,column=0)

#TO ADD BUTTON
button = tkinter.Button(frame,text="Enter data",command=enter_data)
button.grid(row=3,column=0)


window.mainloop()