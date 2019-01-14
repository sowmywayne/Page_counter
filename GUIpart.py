from tkinter import *
from printer import directory

main_windows = Tk()
main_windows.geometry("700x300")
main_windows.title("Page Counter")


def msg():
    i = input_path.get()
    temp = v.get()
    if(temp == 1):
        l2.config(text="Number pages :" + str((directory.docx(i))))
    elif(temp == 2):
        l2.config(text=(directory.pdf(i)))
    else:
        l2.config(text="File Type Is Not Selected")


input_path = StringVar()
v = IntVar()
l1 = Label(main_windows, text="Enter The Path ").place(x=170, y=54)
input_txt_box = Entry(main_windows, textvariable=input_path).place(x=300, y=50)
typFile1 = Radiobutton(
    main_windows,
    text="Docx",
    variable=v,
    value=1).place(
        x=170,
    y=90)
typFile2 = Radiobutton(
    main_windows,
    text="PDF",
    variable=v,
    value=2).place(
        x=300,
    y=90)

b1 = Button(main_windows, text="OK", command=msg).place(x=170, y=140)

l2 = Label(main_windows)
l2.place(x=200, y=170)

main_windows.mainloop()
