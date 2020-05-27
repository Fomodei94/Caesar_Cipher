# Caesar Cipher v1.1
# Author: Fomodei94
# Python, Tk gui library
# Date: 2013-10-19
# Last Update: 2020-05-27

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

def limit_key_size(*args):
  key_value = key.get()
  if len(key_value) > 1: keyValue.set(key_value[1])

app = Tk()
app.title("Caesar Cipher by Fomodei94")
app.geometry("865x320")

Label(app, text = "Plain text:", font = "default 11 bold").grid(row = 0, column = 0, pady = 10)
plain_text = Text(app)
plain_text.config(width = 40, height = 16)
plain_text.grid(row = 1, column = 0, rowspan = 5, padx = 30)

Button(app, text = "Custom key encryption", command = custom_key_encrypt).grid(row = 1, column = 1)
Button(app, text = "Random key encryption", command = random_key_encrypt).grid(row = 2, column = 1, pady = 15)
Label(app, text = "encrypt/decrypt key:").grid(row = 3, column= 1)
keyValue = StringVar()
keyValue.trace('w', limit_key_size)
key = Entry(app, width = 5, font = "default 13 bold", fg = "green", justify = "center", textvariable = keyValue)
key.grid(row = 4, column = 1)
Button(app, text = "Decrypt", command = decrypt).grid(row = 5, column = 1, pady = 10)

Label(app, text = "Encrypted text:", font = "default 11 bold").grid(row = 0, column = 2, pady = 10)
final_text = Text(app)
final_text.config(width = 40, height = 16)
final_text.grid(row = 1, column = 2, rowspan = 5, padx = 30)

app.mainloop()
