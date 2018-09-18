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
        
    def run_game(self):
        # Initialize players
        self.player = Player()
        self.computer = Player()
        self.deal(self.player)
        self.deal(self.computer)
        print (self.player.hand, self.computer.hand)

        print ("YOU ARE PLAYING BLACKJACK! GOOD LUCK!\n")
        playerMove = "h"

        #Game loop
        while (playerMove == 'h'):
            print ("Dealer is showing: [", str(self.computer.hand[0]), "]")
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
                # self.result(player, computer)
                # self.newgame()
            else :
                print ("Wrong move. Please type a valid move statement.")
                playerMove = "h"
                continue





        


# choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
# 		clear()
# 		if choice == "h":
# 			hit(player_hand, deck)
# 			while total(dealer_hand) < 17:
# 				hit(dealer_hand, deck)
# 		elif choice == "s":
# 			while total(dealer_hand) < 17:
# 				hit(dealer_hand, deck)
# 			score(dealer_hand, player_hand)
# 			play_again()
# 		elif choice == "q":
# 			print "Bye!"
# 			exit()


blackjackgame = Blackjack()
blackjackgame.run_game()