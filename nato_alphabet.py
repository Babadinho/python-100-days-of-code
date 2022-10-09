import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_data = {row.letter:row.code for (index,row) in nato_data.iterrows()}

print(new_data)

user_input = input("Enter a new word to get phonetic code: ").upper()

output = [new_data[letter] for letter in user_input]

print(output)