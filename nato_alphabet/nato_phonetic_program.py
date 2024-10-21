import pandas
nato_tbl = pandas.read_csv("nato_phonetic_alphabet.csv")

# also this code can handle, but im not recommend this always
# nato_dict = {letter: code for (letter, code) in nato_tbl.values}

nato_dict = {row.letter: row.code for (index, row) in nato_tbl.iterrows()}

def phonetic_alphabet_maker():
    try:
        user_input = (input("Enter a word: ")).upper()
        encoded_user_input = [nato_dict[letter] for letter in user_input]
        print(encoded_user_input)
    except KeyError:
        print("an illegal character was entered, try again")
        phonetic_alphabet_maker()

phonetic_alphabet_maker()

