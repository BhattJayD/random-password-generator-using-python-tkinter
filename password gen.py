import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.ttk import *
from tkinter import END	
import random

root =tk.Tk()
root.title("Password genrator")
root.configure(background="black")

cwgt=tk.Canvas(root)
cwgt.pack(expand=True, fill=tk.BOTH)
image1=ImageTk.PhotoImage(file="BG.jpeg")
w,h=image1.width(),image1.height()
root.geometry('535x405')




def low(): 
	ent1.delete(0, END) 
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = "" 
	
	length=var1.get()
	
	if var.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(lower) 
		return password 
		
	elif var.get() == 1: 
		for i in range(0, length): 
			password = password + random.choice(upper) 
		return password 
		
	elif var.get() == 2: 
		for i in range(0, length): 
			password = password + random.choice(digits) 
		return password
	else:
		print("select options") 
		
def generate(): 
	password1 = low() 
	ent1.insert(10, password1) 

var=tk.IntVar()
var1=tk.IntVar()


lab1=tk.Label(root,fg="white",bg="blue",text="Password :",cursor='watch').place(x=30,y=60)


    
ent1 = tk.Entry(root,bg="light blue",fg="black")
ent1.place(x=115,y=60)
button1 = tk.Button(root,text='Submit',fg='black',bg= 'orange',height = 1, width = 10,command=generate).place(x=420,y=60)

lab1=tk.Label(root,fg="white",bg="blue",text="strangth :",cursor='watch').place(x=30,y=90)
radio_low = tk.Radiobutton(root, text="Low", variable=var, value=0,bg="light blue").place(x=115,y=90)
radio_medium = tk.Radiobutton(root, text="medium", variable=var, value=1,bg="light blue").place(x=175,y=90)
radio_strong = tk.Radiobutton(root, text="strong", variable=var, value=2,bg="light blue").place(x=264,y=90)


lab1=tk.Label(root,fg="white",bg="blue",text="length :",cursor='watch').place(x=30,y=120)
combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.place(x=115,y=120)

Btn2= tk.Button(root, text="Exit", bg="orange", fg="BLACK",cursor='watch',command=quit).place(x=235,y=370, width=100, height=30)

cwgt.img=image1
cwgt.create_image(0, 0, anchor=tk.NW, image=image1)

root.mainloop()
