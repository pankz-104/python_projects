# method 1 

import string
import random
from tkinter import *

def gen_lowercase():
    s1 = string.ascii_lowercase
    print(''.join(random.choice(s1) for i in range(10)))

def gen_uppercase():
    s2 = string.ascii_uppercase
    print(''.join(random.choice(s2) for i in range(10)))

def gen_letters():
    s3 = string.ascii_letters
    print(''.join(random.choice(s3) for i in range(10)))

def gen_puncutation():
    s4 = string.punctuation
    print(''.join(random.choice(s4) for i in range(10)))

def gen_digits():
    s5 = string.digits
    print(''.join(random.choice(s5) for i in range(10)))

def gen_password():
    s6 = ((string.ascii_letters)+(string.punctuation))
    print(''.join(random.choice(s6) for i in range(10)))
gen_uppercase()
gen_lowercase()

root = Tk()
root.geometry("400x300")
frame = Frame(root)
frame.pack()
button_upper = Button(root,text="generate_upper_password",command=gen_uppercase)
button_upper.pack()
button_lower = Button(root,text="generate_lower_password",command=gen_lowercase)
button_lower.pack()
button_letters = Button(root,text="generate_letters_password",command=gen_letters)
button_letters.pack()
button_punctuation = Button(root,text="generate_punctuation_password",command=gen_puncutation)
button_punctuation.pack()
button_digits = Button(root,text="generate_digits_password",command=gen_digits)
button_digits.pack()
button_mix = Button(root,text="generate_mix_password",command=gen_password)
button_mix.pack()

root.mainloop()



# method 2 

import string
import random
#from tkinter import *

def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = int(input("Enter the password length \n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print(s)

    random.shuffle(s)
    print(s)
    pas = ("".join(s[0:passlen]))
    print(pas)
gen()
