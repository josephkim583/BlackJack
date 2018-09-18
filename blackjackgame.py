import os
import random

class Player:
    def __init__(self):
        self.hand = []

class Blackjack:
    def __init__(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*100


    #Deals cards to the users
    def deal():
        hand = []
        for i in range(2):
            random.shuffle(deck)
            card = self.deck.pop()
            hand.append(card)
        return (hand)
    
    def run_game():
