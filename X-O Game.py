#Author: Islam Hani Awad
#Job: Student at FCAI faculty, Cairo University

from random import randint

class Input(object):
    def choose(Self):
        print("\nPlease Enter Choice(^-^)\n")
        print("[1] Player  Vs  Computer.\n")
        print("[2] Player1 Vs  Player2.\n")
        print("[3] Game Description.\n")
        print("[4] Exit.\n")

        choice = int(input("\nWait For Choice: "))
        return choice
    
    def description(Self):
        print("\nX_O game. A board of 3 x 3 is displayed and one player choses X and the other \nchooses O. Players take turns to put their symbols in an empty cell. The first \nto get one full row, column or diagonal full of his symbol wins. If none does so, it is a draw.\n")
        print("\n -------------------------------------------------------------- \n")

    def printX_O(Self, X_O):
        print("-------------------")
        print("| ", X_O[0], " | ", X_O[1], " | ", X_O[2], " |")
        print("-------------------")
        print("| ", X_O[3], " | ", X_O[4], " | ", X_O[5], " |")
        print("-------------------")
        print("| ", X_O[6], " | ", X_O[7], " | ", X_O[8], " |")
        print("-------------------")
        
#----------------------------------------------------------------------------------------------------------------------------------------

class Player(object):
    def play(Self, name, X_O):
        while True:
            try:
                index = int(input("\nPlayer("+name+") play: "))
                if(X_O[index-1] == index):
                    X_O[index-1] = name
                    obj = Input()
                    obj.printX_O(X_O)
                    return X_O

            except:
                print("Please enter a number")

#----------------------------------------------------------------------------------------------------------------------------------------

class Computer(object):
    def play(Self, X_O):
        while True:
            index = randint(1, 9)
            if(X_O[index-1] == index):
                print("\nComputer(O): ", index)
                X_O[index-1] = "O"
                obj = Input()
                obj.printX_O(X_O)
                return X_O
        
#----------------------------------------------------------------------------------------------------------------------------------------

class Game(object):
    def play(Self, choice):
            X_O = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            counter = 9
            obj = Input()
            obj.printX_O(X_O)
            if(choice == 1):
                player = Player()
                computer = Computer()
                while True:
                    X_O = player.play("X", X_O)
                    counter = counter - 1
                    if((X_O[0]==X_O[1]==X_O[2]=="X") or (X_O[3]==X_O[4]==X_O[5]=="X") or (X_O[6]==X_O[7]==X_O[8]=="X") or (X_O[0]==X_O[3]==X_O[6]=="X") or (X_O[1]==X_O[4]==X_O[7]=="X") or (X_O[2]==X_O[5]==X_O[8]=="X") or (X_O[0]==X_O[4]==X_O[8]=="X") or (X_O[2]==X_O[4]==X_O[6]=="X")):
                        print("\nPlayer IS WIN...\n")
                        break

                    if(counter == 0):
                        print("\nPlayers ARE Draw...\n")
                        break

                    else:
                        X_O = computer.play(X_O)
                        counter = counter - 1
                        if((X_O[0]==X_O[1]==X_O[2]=="O") or (X_O[3]==X_O[4]==X_O[5]=="O") or (X_O[6]==X_O[7]==X_O[8]=="O") or (X_O[0]==X_O[3]==X_O[6]=="O") or (X_O[1]==X_O[4]==X_O[7]=="O") or (X_O[2]==X_O[5]==X_O[8]=="O") or (X_O[0]==X_O[4]==X_O[8]=="O") or (X_O[2]==X_O[4]==X_O[6]=="O")):
                            print("\nPlayer IS LOSE...\n")
                            break
                    
            elif(choice == 2):
                player1 = Player()
                player2 = Player()
                while True:
                    X_O = player1.play("X", X_O)
                    counter = counter - 1
                    if((X_O[0]==X_O[1]==X_O[2]=="X") or (X_O[3]==X_O[4]==X_O[5]=="X") or (X_O[6]==X_O[7]==X_O[8]=="X") or (X_O[0]==X_O[3]==X_O[6]=="X") or (X_O[1]==X_O[4]==X_O[7]=="X") or (X_O[2]==X_O[5]==X_O[8]=="X") or (X_O[0]==X_O[4]==X_O[8]=="X") or (X_O[2]==X_O[4]==X_O[6]=="X")):
                        print("\nPlayer(X) IS WIN...\n")
                        break

                    if(counter == 0):
                        print("\nPlayers ARE Draw...\n")
                        break
                    
                    else:                                
                        X_O = player2.play("O", X_O)
                        counter = counter - 1
                        if((X_O[0]==X_O[1]==X_O[2]=="O") or (X_O[3]==X_O[4]==X_O[5]=="O") or (X_O[6]==X_O[7]==X_O[8]=="O") or (X_O[0]==X_O[3]==X_O[6]=="O") or (X_O[1]==X_O[4]==X_O[7]=="O") or (X_O[2]==X_O[5]==X_O[8]=="O") or (X_O[0]==X_O[4]==X_O[8]=="O") or (X_O[2]==X_O[4]==X_O[6]=="O")):
                            print("\nPlayer(O) IS WIN...\n")
                            break
        
#-----------------------------------------------------------#MAIN#-----------------------------------------------------------------------

while True:
    gm = Game()
    try:
        inp = Input()
        choice = inp.choose()

        if(choice == 3):
            inp.description()

        elif(choice == 4):
            print("\n.... Exiting ....\n")
            break

        else:
            gm.play(choice)

    except:
        print("Please enter a number")
