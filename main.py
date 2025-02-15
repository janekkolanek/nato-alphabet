import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonteic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonteic()
    else:
        print(output_list)

generate_phonteic()
