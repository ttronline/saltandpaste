from tkinter import *

root = Tk()
label = Label(root, text="Do you have salt in your toothpaste?")
label.config(font=("Arial",22))

def click():
    label_2 = Label(root, text="It's good that you have salt!!")
    label_2.config(font=("Arial",18))
    label_2.pack()
def click_2():
    label_3 = Label(root, text="What?? you'd don't salt in your toothpaste, try the new COLGATE!!!")
    label_3.config(font=("Arial",18))
    label_3.pack()

btn = Button(root, text="Yes", width=22, bg="Lime",fg="Indigo",command=click)
btn.config(font=("Cooper Black",13))
btn.grid(row = 1, columns = 1)

btn_2 = Button(root, text="No", width=22, bg="red", fg="Navy Blue", command=click_2)
btn_2.config(font=("Cooper Black",13))
btn.grid(row = 2, columns = 1)

label.pack()
btn_2.pack()
btn.pack()

root.mainloop()
