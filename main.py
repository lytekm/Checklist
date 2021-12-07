import tkinter as tk

tasks = []

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, AddPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def addClick(self, EnternewTask):
        tasks.append(newTask.get())
        print(newTask.get())
        self.show_frame(StartPage)
        EnternewTask.delete(0, 'end')
        StartPage.Update(self)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Title = tk.Label(self, text="Check List")
        Title.grid(row=0, column=0)

        Checklist = tk.Label(self, text="TO DO")
        Checklist.grid(row=1, column=0) 

        addButton = tk.Button(self, text="Add task", command= lambda : controller.show_frame(AddPage))
        addButton.grid(row=2, column=3)

    def Update(self):
        i=0
        for task in tasks:
            chck = tk.Checkbutton(text=task)
            chck.pack()
            chck.grid_rowconfigure(1+i, weight=1)
            chck.grid_columnconfigure(0, weight=1)
            i+=1
            tasks.remove(task)

class AddPage(tk.Frame):

    def __init__(self, parent, controller):
        global newTask
        tk.Frame.__init__(self, parent)

        newTask = tk.StringVar()

        EnternewTask = tk.Entry(self, textvariable=newTask)
        EnternewTask.grid(row=0, column=0)
        Enterbutton = tk.Button(self, text="Add", command= lambda : controller.addClick(EnternewTask))
        Enterbutton.grid(row=1, columnspan=2)




    


app = App()
app.mainloop()