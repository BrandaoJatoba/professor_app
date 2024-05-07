import tkinter as tk
from tkinter import ttk
from frames import HomePage
from teacher import Teacher
from course import Course
from toplevelcourse import CourseWindow, NewCourseWindow

class MainWindow(tk.Tk):

    def __init__(self,  *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Assistente do Professor")
        self.geometry("1024x800")

        menubar = tk.Menu()

        professorMenu = tk.Menu(menubar, tearoff=0)
        professorMenu.add_command(label="Página Inicial", command=None)
        professorMenu.add_command(label="Dados Pessoais", command=None)
        professorMenu.add_command(label="Configurações")
        professorMenu.add_command(label="Sair", command=self.quit)
        menubar.add_cascade(label="Professor", menu=professorMenu)
        self.config(menu=menubar)

        courseMenu = tk.Menu(menubar, tearoff=0)
        courseMenu.add_command(label="Nova Turma", command=self.newCourseWindow)
        courseMenu.add_command(label="Lista de Turmas", command=self.openCourseWindow)
        menubar.add_cascade(label="Turmas", menu=courseMenu)
        self.config(menu=menubar)        

        studentMenu = tk.Menu(menubar, tearoff=0)
        studentMenu.add_command(label="Cadastrar Aluno")
        studentMenu.add_command(label="Lista de Alunos")
        studentMenu.add_command(label="Estatísticas")
        menubar.add_cascade(label="Alunos", menu=studentMenu)
        self.config(menu=menubar)        

        classMenu = tk.Menu(menubar, tearoff=0)
        classMenu.add_command(label="Cadastrar Aula")
        classMenu.add_command(label="Lista de Aulas")
        menubar.add_cascade(label="Aulas", menu=classMenu)
        self.config(menu=menubar)       

        examMenu = tk.Menu(menubar, tearoff=0)
        examMenu.add_command(label="Cadastrar Avaliação")
        examMenu.add_command(label="Notas")
        examMenu.add_command(label="Lista de Avaliações")
        menubar.add_cascade(label="Avaliações", menu=examMenu)
        self.config(menu=menubar)

        scheduleMenu = tk.Menu(menubar, tearoff=0)
        scheduleMenu.add_command(label="Calendário")
        scheduleMenu.add_command(label="Proximos Eventos")
        menubar.add_cascade(label="Calendário", menu=scheduleMenu)
        self.config(menu=menubar)

        # frame = HomePage(self)
    
    def openCourseWindow(self):
        courseWindow = CourseWindow(self)

    def newCourseWindow(self):
        teacherSubmit = NewCourseWindow(self)
        teacherSubmit.lift()

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()