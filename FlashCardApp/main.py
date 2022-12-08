import pandas
from tkinter import *
from google_trans_new import google_translator
import random


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
ROUND_FONT = ("Ariel", 25, "normal")
ROUNDS = 0
GAME_ON = False
SCORE = 0
total_rounds = 20


def end_game():
    global card_canvas, ROUNDS, \
        start_button, round_text, SCORE, total_rounds, \
        cross_button, tick_button, frontcard_img, card_img
    ROUNDS = 0
    card_canvas.itemconfig(word_text, text="Word")
    card_canvas.itemconfig(language_text, text="Language")
    card_canvas.itemconfig(card_img, image=frontcard_img)
    start_button = Button(text="Start", font=ROUND_FONT, command=start_game)
    start_button.grid(column=1, row=2)
    round_text.config(text="Score: {}%".format(round(SCORE * 100 / total_rounds)))
    SCORE = 0
    cross_button.config(state=DISABLED)
    tick_button.config(state=DISABLED)

def next_round_scored():
    global SCORE
    SCORE += 1
    next_round()

def next_round():
    global ROUNDS, spanish_words, total_rounds, \
        tick_button, cross_button, card_img, card_canvas, frontcard_img
    ROUNDS += 1
    card_canvas.itemconfig(card_img, image=frontcard_img)
    cross_button.config(state=DISABLED)
    tick_button.config(state=DISABLED)
    if ROUNDS <= total_rounds:
        update_round_text(ROUNDS)
        ran_word = grab_word(spanish_words)
        card_timer(ran_word)
    else:
        end_game()

def update_round_text(rounds):
    global round_text
    round_text.config(text="Round {} of {}".format(rounds, total_rounds))

def update_game_text(word, language):
    global card_canvas
    card_canvas.itemconfig(word_text, text=word)
    card_canvas.itemconfig(language_text, text=language)

def start_game():
    global start_button, spanish_words, ROUNDS, tick_button, cross_button
    ROUNDS += 1
    ran_word = grab_word(spanish_words)
    card_timer(ran_word)
    start_button.destroy()
    update_round_text(ROUNDS)

def grab_word(word_list):
    ran_word = random.choice(word_list)
    update_game_text(ran_word, "Spanish")
    return ran_word

def card_timer(word):
    global window
    window.after(3000, flip_card, word)

def flip_card(spanish_word):
    global tick_button, cross_button, card_img, backcard_img
    card_canvas.itemconfig(card_img, image=backcard_img)
    tick_button.config(state=NORMAL)
    cross_button.config(state=NORMAL)
    english_word = translate_spanish(spanish_word)
    update_game_text(english_word, "English")

def translate_spanish(spanish_word):
    translator = google_translator()
    translation = translator.translate(spanish_word, lang_src="es", lang_tgt="en")
    return translation
    # translator = Translator(service_urls=["translate.googleapis.com"])
    # translation = translator.translate(text=spanish_word, src="es", dest="el")
    # return translation.text


# Get words
spanish_data = pandas.read_csv("spanish.csv")
spanish_words = spanish_data["Orden"].tolist()

# UI setup
window = Tk()
window.title("Flash Card Application - Spanish")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Text
round_text = Label(font=ROUND_FONT, bg=BACKGROUND_COLOR)
round_text.grid(column=1, row=0)

# Cards
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=False)
backcard_img = PhotoImage(file="images/card_back.png")
frontcard_img = PhotoImage(file="images/card_front.png")
card_img = card_canvas.create_image(400, 263, image=frontcard_img)
word_text = card_canvas.create_text(400, 263, text="Word", font=WORD_FONT)
language_text = card_canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
card_canvas.grid(column=0, row=1, columnspan=3)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=False, command=next_round)
cross_button.config(state=DISABLED)
cross_button.grid(column=0, row=2)

start_button = Button(text="Start", font=ROUND_FONT, command=start_game)
start_button.grid(column=1, row=2)

tick_img = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_img, highlightthickness=False, command=next_round_scored)
tick_button.config(state=DISABLED)
tick_button.grid(column=2, row=2)

# Keep window up
window.mainloop()
