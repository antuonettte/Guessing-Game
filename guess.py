import random

# random.choice(arr)

categories = ["Animals","Countries"]
Animals = ["Tiger", "Giraffe", "Shark", "Snake", "Bunny", "Bear", "Elephant", "Fox", "Panda", "Camel"]
Countries = ["England", "France", "Honduras", "Ecuador", "Yemen", "Sudan", "Korea", "Japan", "Croatia", "Kuwait"]

def play_game():
    print("Pick a category \n")
    print(*categories, sep = ", ")
    print("\n")

    user_choice = input(" ")

    random_word = None
    while True:
        if user_choice.lower() == "animals":
            random_word = random.choice(Animals)
            break
        elif user_choice.lower() == "countries":
            random_word = random.choice(Countries)
            break
        else:
            print("Please choose a valid Category \n")
            user_choice = input(" ")
    

    # print('_' * len(random_word))

    underscore = []

    for letter in random_word:
        underscore.append("_")

    print(*underscore)
    print("\n")
    # print(random_word) for testing purpose

    guesses = 7
    user_Correct = False

    while True:
        print("You have " + str(guesses) + " attempts left")
        user_Correct = False
        user_letter = input("Guess a letter \n")
        for idx, letter in enumerate(random_word.lower()):
            if user_letter == letter:
                underscore[idx] = letter
                print(*underscore)
                print("\n")
                user_Correct = True
            # elif user_letter != letter:
            #     guesses+=1
            #     print(str(guesses) + "<--")
        else:
            if user_Correct != True:
                guesses-= 1
                if guesses == 0:
                    print("HAHA YOU LOSE!")
                    break
                
    
    

        

play_game()