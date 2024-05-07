import tkinter as tk
from tkinter import ttk

from teacher import Teacher
from course import Course

class NewCourseWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("New Course")
        self.geometry("250x125")
        # Labels

        tk.Label(self, text="Title:").grid(row=1, column=0)
        # tk.Label(self, text="Teacher:").grid(row=2, column=0)
        tk.Label(self, text="Schedule:").grid(row=3, column=0)
        tk.Label(self, text="Info:").grid(row=4, column=0)
        tk.Label(self, text="Total Credit Hours:").grid(row=5, column=0)


        # Entry fields
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=1, column=1)

        # teachers = Teacher.get_all()
        # teacher_id_entry = tk.ttk.Combobox(self, state="readonly")
        # names = []
        # for teacher in teachers:
        #     names.append(teacher.name)
        # teacher_id_entry['value'] = [name for name in names]
        # teacher_id_entry.grid(row=2, column=1)

        self.schedule_entry = tk.Entry(self)
        self.schedule_entry.grid(row=3, column=1)

        self.info_entry = tk.Entry(self)
        self.info_entry.grid(row=4, column=1)

        ############################################################################# TO DO! Need to validate entry
        self.total_credit_hours_entry = tk.Entry(self)
        self.total_credit_hours_entry.grid(row=5, column=1)

        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=lambda: self.submit(self))
        self.submit_button.grid(row=7, columnspan=2)
        pass

    def submit(self, toplevelWindow):
        
        title_val = toplevelWindow.title_entry.get()
        teacher_id_val = 0
        schedule_val = toplevelWindow.schedule_entry.get()
        info_val = toplevelWindow.info_entry.get()
        total_credit_hours_val = toplevelWindow.total_credit_hours_entry.get()
        
        if title_val == total_credit_hours_val == "":
            tk.messagebox.showerror("Atention", "Courses must have at least a Title and Credit Hours fields filled.", parent=toplevelWindow)
            # toplevelWindow.lift()
            return

        # You can use the data here as required, for example, print them:
        C1 = Course(title_val, teacher_id_val, total_credit_hours_val, {}, info_val)
        Course.save_instance(C1)

        # You can add further processing of the data here
        tk.messagebox.showinfo("", "Course created successfully.") 

        # Close the window after submitting
        toplevelWindow.destroy()



class CourseWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Janela - Turmas")
        self.geometry("800x600")

        courseFrame = CourseFrame(self)
        courseFrame.grid(column=0, row=0)
    
        ttk.Button(self,text='Close', command=self.destroy).grid_anchor()

class CourseFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        #setup grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        #call widgets
        self.__createWidgets()

    def __createWidgets(self):
        # insert labels and entries here
        ttk.Label(self, text='Find what:').grid(column=0, row=0, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)

        # Replace with:
        ttk.Label(self, text='Replace with:').grid(
            column=0, row=1, sticky=tk.W)
        replacement = ttk.Entry(self, width=30)
        replacement.grid(column=1, row=1, sticky=tk.W)
