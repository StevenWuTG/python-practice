import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return "The word doesnt exist. Please double check it."

word = input("Enter word: ")


print(translate(word))