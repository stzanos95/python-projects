from googletrans import Translator
from tkinter import *


window = Tk()
window.title("Flash Card Application - Spanish")
window.config(padx=50, pady=50)

def grab_word():
    return "es"

def card_timer(word):
    global window
    window.after(4000, flip_card, word)

def flip_card(spanish_word):
    english_word = translate_spanish(spanish_word)
    print(english_word)

def translate_spanish(spanish_word):
    translator = Translator(service_urls=["translate.googleapis.com"])
    translation = translator.translate(text=spanish_word, src="es", dest="el")
    return translation.text


rand_word = grab_word()
card_timer(rand_word)

window.mainloop()
