import os
import random

class Player:
    def __init__(self):
        self.name = ""
        self.cards = []
        self.total = 0
        self.move = "h"

class Blackjack:
    def __init__(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*100
        self.done = False
    
    #Deals cards to the users
    def deal(self, player):
        hand = []
        for i in range(2):
            random.shuffle(self.deck)
            card = self.deck.pop()
            player.cards.append(self.convertcard(card))
            self.summ(player, card)
    
    def convertcard(self, i):
        cards = {11: 'J', 12: "Q", 13: "K", 1: "A"}
        if (i in cards):
            return (cards[i])
        else:
            return (str(i))

    #Sum up the hands of player
    def summ(self, player, card):
        if (card == 1):
            if (player.total >= 11):
                player.total += 1
            else:
                player.total += 11
        elif (card >= 10):
            player.total += 10
        else:
            player.total += card
    
    #Computer move default
    def default(self, player):
        while (player.total < 17):
            self.hit(player)

    #Hit Move
    def hit(self, player):
        card = self.deck.pop()
        player.cards.append(self.convertcard(card))
        self.summ(player, card)

    #Prints the results of the game
    def print_results(self, computer, player):
        # self.clearscreen()
        print (computer.name, " has a " + str(computer.cards) + " for a total of " + str(computer.total))
        print (player.name, " has a " + str(player.cards) + " for a total of " + str(player.total))

    #Determines the results of the game
    def result(self, player, computer):
        if player.total == 21:
            self.print_results(computer, player)
            print (player.name, "wins! ", player.name, " got a Blackjack!!\n")
        elif computer.total == 21:
            self.print_results(computer, player)
            print (computer.name, "wins! ", computer.name, " got a Blackjack!!\n")
        elif player.total > 21:
            self.print_results(computer, player)
            print(player.name, " busted. ", computer.name, "wins!")
        elif computer.total > 21:
            self.print_results(computer, player)
            print(computer.name, " busted. ", player.name, "wins!")
        elif player.total < computer.total:
            self.print_results(computer, player)
            print (computer.name, " wins!!!")
        elif player.total > computer.total:
            self.print_results(computer, player)
            print (player.name, " wins!!!")   
        elif player.total == computer.total:
            self.print_results(computer, player)
            print ("It is a tie!!")

    # Playing again
    def newgame(self):
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == "y":
            self.run_game()
        else:
            print ("THANK YOU FOR PLAYING!")
            exit()
    
    #Clearing screen
    def clearscreen(self):
        if os.name == 'nt':
            os.system('CLS')
        if os.name == 'posix':
            os.system('clear')

    # Single player mode
    def singleplayer(self):
        # Initialize players
        self.player = Player()
        self.computer = Player()
        self.deal(self.player)
        self.deal(self.computer)
        self.clearscreen()
        self.player.name = input("What is your name?: ")
        self.computer.name = "Computer"
        playerMove = "h"
        while (playerMove == 'h'):
            print ("Computer is showing: [", str(self.computer.cards[0]), "]")
            print (self.player.name, " has: ", str(self.player.cards), "Total: ", str (self.player.total))
            playerMove = input("[H]it, [S]tand, [Q]uit: ").lower()

            if (playerMove == 'q'):
                print ("GAME OVER!")
                break
            elif (playerMove == 'h'):
                self.hit(self.player)
                self.default(self.computer)
            elif (playerMove == 's'):
                self.default(self.computer)
                self.result(self.player, self.computer)
                self.newgame()
            else :
                print ("Wrong move. Please type a valid move statement.")
                playerMove = "h"
                continue

    # Multiplayer game loop
    def multiplayer(self):
        self.clearscreen()
        # Initialize players
        self.playerone = Player()
        self.playertwo = Player()
        self.deal(self.playerone)
        self.deal(self.playertwo)

        self.playerone.name = input("What is player 1 name?: ")
        self.playertwo.name = input("What is player 2 name?: ")

        while (self.playerone.move == 'h' or self.playertwo.move == 'h'):
            if (self.playerone.move == 'h'):
                self.clearscreen()
                print ("It is ", self.playerone.name, "'s turn")
                print (self.playertwo.name, " is showing: [", str(self.playertwo.cards[0]), "]")
                print ("You have: ", str(self.playerone.cards), "Total: ", str (self.playerone.total))
                self.playerone.move = input("[H]it, [S]tand, [Q]uit: ").lower()
                if (self.playerone.move == "q"):
                    print ("GAME OVER!")
                    break
                elif (self.playerone.move == 'h'):
                    self.hit(self.playerone)
                else :
                    print ("Wrong move. Please type a valid move statement.")
                    continue

            if (self.playertwo.move == 'h'): 
                self.clearscreen()
                print ("It is ", self.playertwo.name, "'s turn")
                print (self.playerone.name, " is showing: [", str(self.playerone.cards[0]), "]")
                print ("You have: ", str(self.playertwo.cards), "Total: ", str (self.playertwo.total))
                self.playertwo.move = input("[H]it, [S]tand, [Q]uit: ").lower()
                if (self.playertwo.move == "q"):
                    print ("GAME OVER!")
                    break
                elif (self.playertwo.move == 'h'):
                    self.hit(self.playertwo)
                elif (self.playertwo.move == 's'):
                    self.playertwo.move = 's'
                else :
                    print ("Wrong move. Please type a valid move statement.")
                    continue

        self.clearscreen()
        self.result(self.playerone, self.playertwo)
        self.newgame()

    # Game engine
    def run_game(self):
        print ("YOU ARE PLAYING BLACKJACK! GOOD LUCK!\n")        
        setting = input("[S]ingleplayer, [M]ultiplayer, [Q]uit ?").lower()
        if (setting == "s"):
            self.singleplayer()      
        elif (setting == "m"):
            self.multiplayer()           
        elif (setting == "q"):
            print ("GAME OVER!")      
        else:
            self.clearscreen()
            print ("Incorrect input. Please type a valid input")          
            self.run_game()

blackjackgame = Blackjack()
blackjackgame.run_game()