from tkinter import *
from tkinter import messagebox
import base64


def decrypt():
    password = code.get()
    if password == 'Masi123':
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("500x250")
        screen2.configure(bg="lightgreen")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT: ", font="arial", fg="white", bg="grey").place(x=10, y=0)
        text2 = Text(screen2, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=30, width=480, height=200)

        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "Masi123":
        messagebox.showerror("encryption", "Invalid Password")


def encrypt():
    password = code.get()
    if password == 'Masi123':
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("500x250")
        screen1.configure(bg="pink")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT: ", font="arial", fg="white", bg="grey").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=30, width=480, height=200)

        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "Masi123":
        messagebox.showerror("encryption", "Invalid Password")


def window():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x400")
    screen.title("Secret MSG")

    icon_image = PhotoImage(file="Encrypt Logo.png")
    screen.iconphoto(False, icon_image)

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="*Input text below to encrypt or decrypt*", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 18", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="*Enter secret key for encryption and decryption*", fg="black", font=("calbri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=20, bd=0, font=("arial", 25), show="#").place(x=10, y=200)

    Button(text="ENCRYPT", height=2, width=23, bg="red", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="green", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="blue", fg="white", bd=0, command=reset).place(x=10, y=300)

    # Creator Label
    Creator = Label(screen, text="Created by Musa-Iman A.Y.", font="segoe 10 bold italic", bg="white",
                    width=25, bd=5, relief=GROOVE)
    Creator.place(x=90, y=360)

    screen.mainloop()


window()
