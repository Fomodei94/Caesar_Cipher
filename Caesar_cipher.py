# Caesar Cipher v1.1
# Author: Fomodei94
# Python, Tk gui library
# Date: 2013-10-19
# Last Update: 2020-05-24

from random import randint
from tkinter import *

def random_key_encrypt():
   random_key = randint(1, 9)
   key.delete(0,END)
   encrypted_text = ""
   for i in range(len(plain_text.get(1.0, END))):
     encrypted_text += chr(ord(plain_text.get(1.0, END)[i]) + random_key)
   final_text.delete(1.0, END)
   final_text.insert(1.0, encrypted_text)
   key.insert(0, random_key)

def custom_key_encrypt():
    k = int(key.get())
    encrypted_text = ""
    for i in range(len(plain_text.get(1.0, END))):
        encrypted_text += chr(ord(plain_text.get(1.0, END)[i]) + k)
    final_text.delete(1.0, END)
    final_text.insert(1.0, encrypted_text)    

def decrypt():
   decrypted_text = ""
   for i in range(len(final_text.get(1.0, END))):
     decrypted_text += chr(ord(final_text.get(1.0, END)[i]) - int(key.get()))
   plain_text.delete(1.0, END)
   plain_text.insert(1.0, decrypted_text)

app = Tk()
app.title("Caesar Cipher by Fomodei94")
app.geometry("600x800")
Label(app, text = "Text to be encrypted:").pack(pady = 10)
plain_text = Text(app)
plain_text.pack(padx = 30)
Button(app, text = "Custom key encryption", command = custom_key_encrypt).pack(padx = 5, pady = 10)
Button(app, text = "Random key encryption", command = random_key_encrypt).pack(anchor = "center")
Label(app, text = "encrypt/decrypt key:").pack(pady = 7)
key = Entry(app, width = 5, font = "default 13 bold", fg = "darkgreen", justify = "center")
key.pack()
Button(app, text = "Decrypt", command = decrypt).pack(anchor = "center", pady = 7)
Label(app, text = "Encrypted text:").pack(pady = 5)
final_text = Text(app)
final_text.pack(padx = 30, pady = 7)
app.mainloop()
