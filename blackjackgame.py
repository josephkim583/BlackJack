import os
import random

class Player:
    def __init__(self):
        self.hand = []
        self.total = 0

class Blackjack:
    def __init__(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*100

    #Deals cards to the users
    def deal(self, player):
        hand = []
        for i in range(2):
            random.shuffle(self.deck)
            card = self.deck.pop()
            player.hand.append(card)
            self.summ(player, card)
    
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
    
    #Computer default mode
    def default(self, player):
        while (player.total < 17):
            self.hit(player)

    #Hit Move
    def hit(self, player):
        card = self.deck.pop()
        player.hand.append(card)
        self.summ(player, card)

    #Prints the results of the game
    def print_results(self, computer, player):
        self.clearscreen()
        print ("The computer has a " + str(computer.hand) + " for a total of " + str(computer.total))
        print ("You have a " + str(player.hand) + " for a total of " + str(player.total))

    #Determines the results of the game
    def result(self, player, computer):
        if player.total == 21:
            self.print_results(computer, player)
            print ("Congratulations! You got a Blackjack!\n")
        elif computer.total == 21:
            self.print_results(computer, player)
            print ("Sorry, you lose. The computer got a blackjack.\n")
        elif player.total > 21:
            self.print_results(computer, player)
            print ("Sorry. You busted. You lose.\n")
        elif computer.total > 21:
            self.print_results(computer, player)
            print ("Computer busts. You win!\n")
        elif player.total < computer.total:
            self.print_results(computer, player)
            print ("Sorry. Your score isn't higher than the computer. You lose.\n")
        elif player.total > computer.total:
            self.print_results(computer, player)
            print ("Congratulations. Your score is higher than the computer. You win\n")
    
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

    # Game engine
    def run_game(self):
        # Initialize players
        self.player = Player()
        self.computer = Player()
        self.deal(self.player)
        self.deal(self.computer)
        print ("YOU ARE PLAYING BLACKJACK! GOOD LUCK!\n")

        playerMove = "h"
        setting = input("[S]ingleplayer, [M]ultiplayer, [Q]uit ?").lower()
        #Game loop
        if (setting == "s"):
            while (playerMove == 'h'):
                print ("Computer is showing: [", str(self.computer.hand[0]), "]")
                print ("Player has: ", str(self.player.hand), "Total: ", str (self.player.total))
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
        elif (setting == "q"):
            print ("GAME OVER!")
        
        else:
            self.clearscreen()
            print ("Incorrect input. Please type a valid input")          
            self.run_game()

blackjackgame = Blackjack()
blackjackgame.run_game()