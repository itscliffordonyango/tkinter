"""
 Student Grading App
This is a simple GUI app that gets students inputs , then evaluates the input to give the student a grade and remarks of the lecturer

define the variables we will use 

Student_name = ""
Student_id = ""
Student_score = 0
Student_grade = ""
Lecturer_remarks = ""

----Grade ranges----
0 - 39 = F
40 - 49 = D
50 - 59 = C
60 - 69 = B
70 - 90 = A
91 - 100 = O  (outstanding)

----Lecturer remarks----
F= "Fail"
D= "Poor"
C= "Average"
B= "Good"
A= "Very Good"
O= "Outstanding"

"""

  
import tkinter as tk
from tkinter import messagebox

#  process and grade the student
def student_form():
    Student_id = ID_entry.get()
    Student_name = name_entry.get()
    try:
        Student_score = int(score_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric score!")
        return

    if 0 <= Student_score <= 39:
        Student_grade = "F"
        Lecturer_remarks = "Fail"
    elif 40 <= Student_score <= 49:
        Student_grade = "D"
        Lecturer_remarks = "Poor"
    elif 50 <= Student_score <= 59:
        Student_grade = "C"
        Lecturer_remarks = "Average"
    elif 60 <= Student_score <= 69:
        Student_grade = "B"
        Lecturer_remarks = "Good"
    elif 70 <= Student_score <= 90:
        Student_grade = "A"
        Lecturer_remarks = "Very Good"
    elif 91 <= Student_score <= 100:
        Student_grade = "O"
        Lecturer_remarks = "Outstanding"
    else:
        messagebox.showerror("Score Error", "Score must be between 0 and 100")
        return

    # Save to file
    with open("student_records.txt", "a") as file:
        file.write(f"{Student_id},{Student_name},{Student_score},{Student_grade},{Lecturer_remarks}\n")

    # Show result in popup window
    show_result_popup(Student_id,
                      Student_name,
                      Student_score,
                      Student_grade,
                      Lecturer_remarks)

# clear the form
def clear_form():
    ID_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)

# display results in popup
def show_result_popup(sid, name, score, grade, remark):
    popup = tk.Toplevel(mainwindow)
    popup.title("Student Result")
    popup.geometry("400x250")
    popup.config(bg="#0a093f")

    tk.Label(
        popup,
        text="Student Result",
        font=("Arial", 16, "bold"),
        bg="#0a093f",
        fg="white").pack(pady=10)

    result_text = f"""
    ID: {sid}
    Name: {name}
    Score: {score}
    Grade: {grade}
    Remarks: {remark}
    """
    tk.Label(
        popup,
        text=result_text,
        font=("Arial", 12),
        justify="left",
        bg="#0a093f",
        fg="#69f5ff").pack(pady=10)

    tk.Button(
        popup,
        text="Close",
        command=popup.destroy,
        bg="#f54254",
        fg="white",
        font=("Arial", 10, "bold")).pack(pady=10)

# Main window 
mainwindow = tk.Tk()
mainwindow.title("Student Grading App")
mainwindow.geometry("1000x650")
mainwindow.config(bg="#000b6b")

# Form Frame
form = tk.Frame(
    mainwindow,
    bg="#000b6b",
    padx=20,
    pady=20)
form.pack(pady=50)

# Student ID
tk.Label(
    form,
    text="Student ID",
    bg="#000b6b",
    fg="white",
    font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
ID_entry = tk.Entry(form, font=("Arial", 12))
ID_entry.grid(row=0, column=1, pady=5)

# Student Name
tk.Label(
    form,
    text="Student Name",
    bg="#000b6b",
    fg="white",
    font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form, font=("Arial", 12))
name_entry.grid(row=1, column=1, pady=5)

# Student Score
tk.Label(
    form,
    text="Student Score",
    bg="#000b6b",
    fg="white",
    font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
score_entry = tk.Entry(form, font=("Arial", 12))
score_entry.grid(row=2, column=1, pady=5)

# Submit Button
submit = tk.Button(
    form,
    text="Submit",
    command=student_form,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold")
)
submit.grid(row=3, column=0, pady=20)

# Clear Button
clear = tk.Button(
    form,
    text="Clear",
    command=clear_form,
    bg="#f0ad4e",
    fg="white",
    font=("Arial", 12, "bold")
)
clear.grid(row=3, column=1, pady=20)


mainwindow.mainloop()

