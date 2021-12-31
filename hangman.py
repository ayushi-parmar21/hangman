import random
def hungman():
    
    list_of_word= ["hello","park","shop","ayushi","india"]
    word = random.choice(list_of_word)
    print(word)
    turns = 10
    guessmade=""
    valid_entry=set("abcdefghijklmnopqrstuvwxy")
    
    while len(word)>0:
        main_world=""
        missed=0
        
        for letter in word:
            if letter in guessmade:
                main_world+=letter
            else:
                main_world+="_ "
        if main_world==word:
            print("you won!!!!")
            print("do you want to play this game: ")
            user2=input("enter yes or no: ")
            if user2=="yes":
                hungman()
            else:
                break
            
        print("guess the word",main_world)
        guess=input("enter a letter: ")
        
        if guess in valid_entry:
            guessmade+=guess
        else:
            print("enter valid character:'")
            guess=input()
        if guess not in word:
            turns-=1
            
            if turns==9:
                print("9 turn left!!!!!!")
                print("  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            if turns==8:
                 print("8 turn left!!!!!!")
                 print("   _____ \n"
                       "  |      \n"
                       "  |      \n"
                       "  |      \n"
                       "  |      \n"
                       "  |      \n"
                       "  |      \n"
                       "__|__\n")
            if turns==7:
                print("7 turn left!!!!!!")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            if turns==6:
                print("6 turn left!!!!!!")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            if turns==5:
                print("5 turn left!!!!!!")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     O \n"
                      "  |     | \n"
                      "  |       \n"
                      "  |      \n"
                      "__|__\n")
            if turns==4:
                print("4 turn left!!!!!!")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     O \n"
                      "  |     |\ \n"
                      "  |       \n"
                      "  |      \n"
                      "__|__\n")
            if turns==3:
                print("3 turn left!!!!!!")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     O\n"
                      "  |    /|\ \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            if turns==2:
                print("2 turn left!!!!!!")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     O \n"
                      "  |    /|\  \n"
                      "  |      \ \n"
                      "  |      \n"
                      "__|__\n")
            if turns==1:
                print("1 turn left!!!!!!")
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "  |      \n"
                      "__|__\n")
            if turns==0:
                print("you lose ")
                print("do you want to play this game: ")
                user2=input("enter yes or no: ")
                if user2=="yes":
                    hungman()
                else:
                    break
user_name=input("Enter your name play: ")
print("\n","_"*25+"WELLCOME",user_name,"_"*25)
print("****Try to guess the word in 10 attempts*****")
hungman()