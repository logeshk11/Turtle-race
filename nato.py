import pandas
nato=pandas.read_csv("nato_phonetic_alphabet.csv")
word=input("entr the word").upper()
new_dic={row.letter:row.code for(index, row) in nato.iterrows()}

for a in word:
    print(f"{a}-{new_dic[a]} ")