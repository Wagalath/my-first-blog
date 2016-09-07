import donnees
import random

def recup_name():
    name=input('enter name ')
    return name

def initialize_data():
    authorized_words=donnees.liste_mots
    number_max=donnees.nb_chances
    return (authorized_words,number_max)

def choice_of_word(authorized_words):
    i=0
    word=list(authorized_words[int(len(authorized_words)*random.random())])
    word_found=[]
    while i<len(word):
        word_found.append('?')
        i+=1
    return (word,word_found)

def trial(word_chosen, word_found):
    global remaining_trials
    letter = input('enter a letter')
    if letter.lower() in word_chosen:
        i=0
        while i<len(word_chosen):
            if letter==word_chosen[i]:
                word_found[i]=letter
            i+=1
        print('the letter ', letter, 'is in the researched word and the word can be written ', ''.join(word_found))
    else:
        remaining_trials-=1
        print('the letter ', letter, 'is not in the researched word; the word can be written ', ''.join(word_found))


if __name__ == '__main__':
    recup_name()
    (authorized_words,number_max)=initialize_data()
    remaining_trials=number_max
    (word_chosen,word_found)=choice_of_word(authorized_words)
    print(word_chosen)

    while remaining_trials>0:
        trial(word_chosen, word_found)
        if word_chosen==word_found:
            print('you won and your score is ', remaining_trials)
            break

