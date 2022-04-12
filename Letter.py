import random
def hangman():
    list_of_words = ['india','swithzerland','persia','egypt','chile','pakistan'
                    'sriLanka','australia']
    word = random.choice(list_of_words)
    guessmade = ""
    turns = 10
    valid_entry = set('abcdefghijklmnopqrstvuwxyz')
    while True:
        main_word = ""
        guess_word = ""
        

        for letter in word:
            if letter in guessmade:
                main_word = main_word + " " + letter
                guess_word = guess_word + letter

            else:
                main_word = main_word +" "+ "_"

        if guess_word == word:
            print("You win!!!")
            print(word)
            break;
            
        print("guess the words ",main_word)
        guess = input()

        while guess not in valid_entry or guess in guessmade:
            if guess in guessmade:
                print("Already you guessed the word")
            print("Enter the valid character")
            guess = input()

    
        if guess in valid_entry and guess not in guessmade:
            guessmade = guessmade + guess
        
        

        if guess not in word:
            turns = turns-1
            
            if turns==9:
                print("9 turns left!!!")
                print("---------------")
            
            if turns == 8:
                print("8 turns left!!!")
                print("---------------")
                print("       o       ")

            if turns == 7:
                print("7 turns left!!!")
                print("---------------")
                print("       o       ")
                print("       |       ")

            if turns == 6:
                print("6 turns left!!!")
                print("---------------")
                print("       o       ")
                print("       |       ")
                print("      /        ")

            if turns == 5:
                print("5 turns left!!!")
                print("---------------")
                print("       o       ")
                print("       |       ")
                print("      / \      ")

            if turns == 4:
                print("4 turns left!!!")
                print("---------------")
                print("       o       ")
                print("       |       ")
                print("      / \      ")

            if turns == 4:
                print("4 turns left!!!")
                print("---------------")
                print("      \o       ")
                print("       |       ")
                print("      / \      ")
            
            if turns == 3:
                print("3 turns left!!!")
                print("---------------")
                print("      \o/       ")
                print("       |       ")
                print("      / \      ")

            if turns == 2:
                print("2 turns left!!!")
                print("---------------")
                print("      \o/ |   ")
                print("       |       ")
                print("      / \      ")

            if turns == 1:
                print("1 turns left!!! Hangman on Last Breathe")
                print("---------------")
                print("      \o/_|   ")
                print("       |       ")
                print("      / \      ")

            if turns == 0:
                print("You Lose!!!")
                print("You made a Good man die")
                print("---------------")
                print("       o_|   ")
                print("      /|\       ")
                print("      / \      ")
                break;
        


name = input("Enter your name")
print("Welcome",name,"!")
print("------------------------------")
print("try to guess the word in less than ten attempts")
hangman()