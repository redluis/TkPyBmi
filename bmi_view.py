import tkinter as tk
from tkinter import messagebox

from bmi_controller import BmiController

class BmiView:
    def __init__(self):
        def more_than_zero_check(input):
            if not input.isdigit():
                return False
            if int(input) <= 0:
                return False
            return True

        def show_bmi():
            try:
                height = int(self.height_entry.get())
                mass = int(self.mass_entry.get())
            except ValueError:
                messagebox.showerror(
                    title='Error',
                    message='Please, enter correct values'
                )
                return
            mess = self.bmi_controller.get_conclusion(mass, height)
            messagebox.showinfo(
                title='Result',
                message=mess
            )

        self.bmi_controller = BmiController() 

        self.w = tk.Tk()
        self.w.title('BMI by MacGregory')
        self.w.geometry('300x200')
        self.w.resizable(False, False)
        self.w.eval('tk::PlaceWindow . center')

        validate = self.w.register(more_than_zero_check)

        self.height_label = tk.Label(self.w, text='Height (sm):', fg='black', pady=10)
        self.height_label.pack()
        self.height_entry = tk.Entry(self.w, fg='black', bg='white', 
            validate='key', validatecommand=(validate, '%P')
        ) 
        self.height_entry.pack()

        self.mass_label = tk.Label(self.w, text='Mass (kg):', fg='black', pady=10)
        self.mass_label.pack()
        self.mass_entry = tk.Entry(self.w, fg='black', bg='white', 
            validate='key', validatecommand=(validate, '%P')
        )
        self.mass_entry.pack()

        self.find_button = tk.Button(self.w, text='Find bmi', fg='black', bg='white', 
            pady=3, padx=5, command=show_bmi
        )
        self.find_button.pack()

        self.w.mainloop()
        