import random

class Blackjack:
    def __init__(self):
        self.deck_of_cards = []
        self.list_of_suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.dcards = []
        self.pcards = []
        self.dealer_sum = 0
        self.player_sum = 0

    # Shuffle Cards

    def card_shuffle(self):
        for suit in self.list_of_suits:
            for card_value in range(1,14):
                self.deck_of_cards.append((suit, card_value))

        random.shuffle(self.deck_of_cards)


    # Dealing Dealer Cards

    def ddealer(self):
        self.dealer_sum = 0
        while len(self.dcards) != 2:
            self.dcards.append(self.deck_of_cards.pop())
        if len(self.dcards) == 2:
            print("The Dealer has Blank Card & ", str((self.dcards[1])) + "\n")
        
        self.dealer_sum += self.dcards[0][1]
        #self.dealer_sum += self.dcards[-1][1]

    # Dealing Player Cards
    
    def pdealer(self):
        while len(self.pcards) != 2:
            self.pcards.append(self.deck_of_cards.pop())
        if len(self.pcards) == 2:
            print("You have", self.pcards)

        self.player_sum += self.pcards[0][1]
        self.player_sum += self.pcards[-1][1]


    # Dealer Total/Sum

    def totaldealer(self):
        for dval in self.dcards:
            self.dealer_sum += dval[1]
        if self.dealer_sum == 21:
            print("Dealer has 21! ")
        elif self.dealer_sum > 21:
            print("Dealer has busted! \n")

    # Player Move/Action

    def player_action(self):
        self.answer = input("What would you like to do?  'H' for HIT, 'S' for STAND:  ").lower()


    def player_action1(self):

        # HIT ACTION
        
        if self.answer == 'h':
            self.pcards.append(self.deck_of_cards.pop())

            self.player_sum += self.pcards[-1][1]
            print("You now have " + str(self.player_sum) + " from the cards below: " + str(self.pcards))

            if self.player_sum > 21:
                print("You busted! \n")
            
            elif self.player_sum == 21:
                pass
                


        # STAND ACTION        

    def player_action2(self):

        if self.answer == 's':
            while self.dealer_sum <= 16:
                self.dcards.append(self.deck_of_cards.pop())
                self.dealer_sum += self.dcards[-1][1]
                break

            print("Here are the Dealers cards: " + str(self.dcards) + "\n")
            print("Dealer has " + str(self.dealer_sum) + "\n")


    # RESULTS

    def results_dealer(self):
        if self.dealer_sum < 22 and self.dealer_sum > self.player_sum:
            print("Here is the result:  The Dealer has won! \n")

        
        print("Here are the dealers cards: " + str(self.dcards) + "\n")
        print("You have " + str(self.player_sum) + "\n")
        print("Here are your cards: " + str(self.pcards) + "\n")

    def results_player(self):

        if self.player_sum < 22 and self.player_sum > self.dealer_sum:
            print("Here is the result:  You have won! \n")
            

        

    def results_tie(self):

        if self.player_sum  == self.dealer_sum and self.player_sum < 22:
            print("You have " + str(self.player_sum))
            print("Dealer has " + str(self.dealer_sum))
            print("Here is the result: You Tied (push) \n")

        if self.player_sum == 21:
            print("You have 21!")

        if self.dealer_sum == 21:
            print("Dealer has 21!")

    def run(self):
        print("You are about to play a game of BlackJack! \n")

        


        self.card_shuffle()
        self.ddealer()
        self.pdealer()
        

        while True:
            self.player_action()
            if self.answer == 's':
                break
            self.player_action1()
        self.totaldealer()
        self.player_action2()
        self.results_dealer()
        self.results_player()
        self.results_tie()

        
        


# game = Blackjack()
# game.run()