import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getMeaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Do you mean %s ? if yes then press Y otherwise N : " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Your word is not %s " % get_close_matches(word, data.keys())[0]
        else :
            return "We couldn't understand!" 
    else:
        return "The word you entered is not existed. Please double check it." 

word = input("Enter a word : ")
output = getMeaning(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)