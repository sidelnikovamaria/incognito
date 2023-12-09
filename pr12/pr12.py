import requests
import json
from tkinter import *
import tkinter as tk
from pprint import pprint
window=Tk()
window.title('Json')
window.geometry('600x300')
e=Entry(window,width=15)
l=Label(window,text='Введите имя пользователя:')
l.pack()
e.pack()
def f():
    a=e.get()
    username=a
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    pprint(user_data)
    data={}
    k=['company','created_at','email','id','name','url']
    for i in k:
        data[i]=user_data[i]
    with open("data_file.json","w") as r:
        json.dump(data,r,indent=4)
bt=Button(window,text="Старт!",command=f,width=45)
bt.pack()
window.mainloop()