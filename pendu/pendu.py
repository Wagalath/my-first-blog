import functions

if __name__ == '__main__':
    functions.recup_name()
    (authorized_words,number_max)=functions.initialize_data()
    remaining_trials=number_max
    (word_chosen,word_found)=functions.choice_of_word(authorized_words)
    print(word_chosen)

    i=0
    while i<number_max:
        functions.trial(word_chosen, word_found)
        i+=1
    
    print ('hello')
