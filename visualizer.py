import tkinter as tk
from tkinter import *
from random import randint
from playsound import playsound  

master = Tk()
lab = Label(master)
lab.pack()

canvas = tk.Canvas(master, width=450, height=300, bg="white")

difect_types = ['foro','goccia']
red_shape = canvas.create_oval(10, 10, 110, 110, fill="white")
green_shape = canvas.create_oval(120, 10, 220, 110, fill="white")
canvas.pack()


def get_plc_message(directory = 'messages.txt'):
    '''
    legge i messaggi scritti da server.py
    che legge i messaggi da PLC e li salva.
    questa funzione legge il file, se presente dei dati,
    prende la prima riga (regola First In First Out)
    e lo restituisce al fine di salvare la id del pezzo.
    '''
    with open(directory, '+r') as f:
        first_line = f.readline()
        lines = f.readlines()

    with open(directory, '+w') as f:       
        if lines[1:]:
            f.writelines(lines)
    
    return first_line

def update():
    TEXT_MESSAGE = get_plc_message('defects_founded.txt')
    lab['text'] = TEXT_MESSAGE
    master.after(3000, update) # run itself again after 1000 ms
    
    have_defects = False
    for difect_type in difect_types:
        if difect_type in TEXT_MESSAGE:
            have_defects = True

    if have_defects:
        canvas.itemconfig(red_shape, fill="red")
        canvas.itemconfig(green_shape, fill="white")
        playsound(".\documents\music\music2.wav")

    else:
        canvas.itemconfig(green_shape, fill="green")
        canvas.itemconfig(red_shape, fill="white")

# run first time
update()

master.mainloop()