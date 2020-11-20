import json
import random

def read_values_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values

def clean_strings(sentences):
    cleaned = []
    for sentence in sentences:
        clean_sentence = sentence.strip()
        cleaned.append(clean_sentence)
    return cleaned

def random_item_in(object_list):
    rand_numb = random.randint(0, len(object_list) - 1)
    return object_list[rand_numb]

def random_value(source_path, key):
    all_values = read_values_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return random_item_in(clean_values)

#####################
###### QUOTES #######
#####################

def random_quote():
    return random_value('quotes.json', 'quote')

######################
#### CHARACTERS ######
######################

def random_character():
    return random_value('characters.json', 'character')

######################
#### INTERACTION #####
######################

def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character, rand_quote))

def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre citation ?'
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break

if __name__ == '__main__':
    main_loop()