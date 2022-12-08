import pandas


nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato_dataframe.iterrows()}
word = input("Which word do you want to spell out?\n").upper()
print([nato_dict[letter] for letter in word])
