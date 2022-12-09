#Program: Eligibility scoring software
#Author: Uzair
#Description: The code takes the input from the user and using an array, it stores the corresponding number with the input
#The code then finds the smallest number and using a popup, a statement is shown in accordance to it.

from tkinter import *
import tkinter as tk
master = tk.Tk()
master.title("Grade Calculator")
master.geometry("700x250")

part1 = tk.Entry(master)
part2 = tk.Entry(master)
part3 = tk.Entry(master)
part4 = tk.Entry(master)
part5 = tk.Entry(master)
part6 = tk.Entry(master)

grading = [10, 20]

def show():
    top = Toplevel(master)
    top.geometry("350x125")
    top.title("Results")
    Label(top, text="Marks Calculator")
    if part3.get() == "fail":
        grading.append(1)

    if part3.get() == "pass":
        grading.append(2)

    if part3.get() == "merit":
        grading.append(3)

    if part3.get() == "distinction":
        grading.append(4)

    if part4.get() == "fail":
        grading.append(1)

    if part4.get() == "pass":
        grading.append(2)

    if part4.get() == "merit":
        grading.append(3)

    if part4.get() == "distinction":
        grading.append(4)

    if part5.get() == "fail":
        grading.append(1)

    if part5.get() == "pass":
        grading.append(2)

    if part5.get() == "merit":
        grading.append(3)

    if part5.get() == "distinction":
        grading.append(4)

    if part6.get() == "fail":
        grading.append(1)

    if part6.get() == "pass":
        grading.append(2)

    if part6.get() == "merit":
        grading.append(3)

    if part6.get() == "distinction":
        grading.append(4)

    minimum = grading[0]
    for i in range(len(grading)):
        if grading[i] < minimum:
            minimum = grading[i]

    if minimum == 1:
        tk.Label(top, text="              Fail").grid(row=12, column=3)
        tk.Label(top, text="               You are Ineligible for internship and scholarship").grid(row=14, column=3)

    if minimum == 2:
        tk.Label(top, text="Pass and above in all units").grid(row=8, column=3)
        tk.Label(top, text="  You are eligible for category 3 of internships and scholarships").grid(row=9, column=3)

    if minimum == 3:
        tk.Label(top, text="Merit and above in all units").grid(row=8, column=3)
        tk.Label(top, text="  You are eligible for category 2 of internships and scholarships").grid(row=9, column=3)

    if minimum == 4:
        tk.Label(top, text="Distinction in all units").grid(row=8, column=3)
        tk.Label(top, text="  You are eligible for category 1 of internships and scholarships").grid(row=9, column=3)

    def end():
        top.destroy()
        master.destroy()
    button2 = tk.Button(top, text="Done", bg="purple", command=lambda: end())
    button2.place(x=140, y=75)

tk.Label(master, text="Name").grid(row=0, column=0)
tk.Label(master, text="Level").grid(row=1, column=0)
tk.Label(master, text="Unit No.").grid(row=2, column=0)
tk.Label(master, text="1").grid(row=3, column=0)
tk.Label(master, text="3").grid(row=4, column=0)
tk.Label(master, text="4").grid(row=5, column=0)
tk.Label(master, text="6").grid(row=6, column=0)
tk.Label(master, text="Subject").grid(row=2, column=1)
tk.Label(master, text="Information Technology Systems").grid(row=3, column=1)
tk.Label(master, text="Social Media in Business").grid(row=4, column=1)
tk.Label(master, text="Programming").grid(row=5, column=1)
tk.Label(master, text="Website Development").grid(row=6, column=1)
tk.Label(master, text="Enter").grid(row=2, column=2)
part3.grid(row=3, column=2)
part4.grid(row=4, column=2)
part5.grid(row=5, column=2)
part6.grid(row=6, column=2)
part1 = tk.Entry(master)
part2 = tk.Entry(master)
part1.grid(row=0, column=1)
part2.grid(row=1, column=1)
button1 = tk.Button(master, text="Submit", bg="purple",command =lambda :show())
button1.grid(row=8, column=1)

master.mainloop()
