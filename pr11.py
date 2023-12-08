from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox, Radiobutton
from tkinter import filedialog
def result_click():
    if znaki.get() == '+':
        res = int(first_num.get())+int(second_num.get())
        result_lbl.configure(text=str(res))
    elif znaki.get() == '-':
        res = int(first_num.get())-int(second_num.get())
        result_lbl.configure(text=str(res))
    elif znaki.get() == '*':
        res = int(first_num.get())*int(second_num.get())
        result_lbl.configure(text=str(res))
    elif znaki.get() =='/':
        res = int(first_num.get())//int(second_num.get())
        result_lbl.configure(text=str(res))
root = Tk()
root.title('Сидельникова Мария Романовна')
root.geometry('500x450')
tab_control = ttk.Notebook(root)
calculator_tab = ttk.Frame(tab_control)
tab_control.add(calculator_tab, text='Калькулятор')
calculator_lbl = Label(calculator_tab)
calculator_lbl.grid(column=0, row=0)
first_num = Entry(calculator_lbl, width=10)
first_num.grid(column=0, row=0)
znaki = Combobox(calculator_lbl, width=3)
znaki ['values'] = ('+', '-', '*', '/')
znaki.grid(column=1, row=0)
second_num = Entry(calculator_lbl, width=10)
second_num.grid(column=2, row=0)
result_button = Button(calculator_lbl, width=3, text='=', command=result_click)
result_button.grid(column=3, row=0)
def check_butt():
    messagebox.showinfo('', 'Поздравляем! Вы выбрали: {} вариант'.format(selected.get()))

tab_control.pack(expand=2, fill='both')
result_lbl = Label(calculator_lbl, width=5)
result_lbl.grid(column=4, row=0)
check_box_tab = ttk.Frame(tab_control)
tab_control.add(check_box_tab, text='Чекбоксы')
selected = IntVar()
check_but1 = Radiobutton(check_box_tab, text='Первый', value=1, variable=selected)
check_but1.grid(column=0, row=0)
check_but2 = Radiobutton(check_box_tab, text='Второй', value=2, variable=selected)
check_but2.grid(column=1, row=0)
check_but3 = Radiobutton(check_box_tab, text='Третий', value=3, variable=selected)
check_but3.grid(column=2, row=0)
check_button = Button(check_box_tab, text='Кнопка', width=10, command=check_butt)
check_button.grid(column=0, row=1)
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text =file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
txt_tab = ttk.Frame(tab_control)
tab_control.add(txt_tab, text='Работа с текстом')
text_editor = Text(txt_tab)
text_editor.grid(column=0, columnspan=2, row=1)
open_button = ttk.Button(txt_tab, text="Открыть файл", command=open_file)
open_button.grid(column=0, row=0, sticky=NSEW, padx=10)
save_button = ttk.Button(txt_tab, text="Сохранить файл", command=save_file)
save_button.grid(column=1, row=0, sticky=NSEW, padx=10)
root.mainloop()
