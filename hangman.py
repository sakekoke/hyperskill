def hangman():
    import random
    langs = ['python', 'java', 'kotlin', 'javascript']
    computer_choice = random.choice(langs)
    letters = set(computer_choice)
    help_word = '-' * len(computer_choice)
    done_letters = set()
    count = 0
    while True:
        print(f'\n{help_word}')
        guess = input('Input a letter: ')
        if len(guess) == 1:
            if guess.islower():
                if guess in done_letters:
                        print('You already typed this letter')
                else:
                    if guess in letters:   
                        for i in range(computer_choice.count(guess)):
                            position = computer_choice.find(guess)
                            help_word = help_word[:position] + guess + help_word[position+1:]
                            if help_word == computer_choice:
                                print(f'You guessed the word {computer_choice}!')
                                print('You survived!')
                                break
                    else:
                        print('No such letter in the word')
                        count += 1
                        if count == 8:
                            print('You are hanged!')
                            break
                    done_letters.add(guess)
            else:
                print('It is not an ASCII lowercase letter')
        else:
            print('You should print a single letter')
print('H A N G M A N\n')
while True:
    play_exit = input('Type "play" to play the game, "exit" to quit: ')
    if play_exit == 'play':
        print(hangman())
    elif play_exit == 'exit':
        break
    else:
        continue