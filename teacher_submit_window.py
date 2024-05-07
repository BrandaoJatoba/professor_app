import tkinter as tk
from tkinter import ttk
from teacher import Teacher
from course import Course

def submit(teachers: list[Teacher]):
    
    title_val = title_entry.get()
    teacher_id_val = teachers[teacher_id_entry.current()].id
    schedule_val = schedule_entry.get()
    info_val = info_entry.get()
    total_credit_hours_val = float(total_credit_hours_entry.get())
    
    # You can use the data here as required, for example, print them:
    C1 = Course(title_val, teacher_id_val, total_credit_hours_val, {}, info_val)
    Course.save_instance(C1)
    for each in Course.get_all():
        print(each)
    # You can add further processing of the data here
    
    # Close the window after submitting
    root.destroy()

teachers = Teacher.get_all()

root = tk.Tk()
root.title("Input Window")

# Labels

tk.Label(root, text="Title:").grid(row=1, column=0)
tk.Label(root, text="Teacher:").grid(row=2, column=0)
tk.Label(root, text="Schedule:").grid(row=3, column=0)
tk.Label(root, text="Info:").grid(row=4, column=0)
tk.Label(root, text="Total Credit Hours:").grid(row=5, column=0)


# Entry fields
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1)

teacher_id_entry = tk.ttk.Combobox(root, state="readonly")
names = []
for teacher in teachers:
    names.append(teacher.name)
teacher_id_entry['value'] = [name for name in names]
teacher_id_entry.grid(row=2, column=1)

schedule_entry = tk.Entry(root)
schedule_entry.grid(row=3, column=1)

info_entry = tk.Entry(root)
info_entry.grid(row=4, column=1)

total_credit_hours_entry = tk.Entry(root)
total_credit_hours_entry.grid(row=5, column=1)



# Submit button
submit_button = tk.Button(root, text="Submit", command=lambda: submit(teachers))
submit_button.grid(row=7, columnspan=2)


root.mainloop()
