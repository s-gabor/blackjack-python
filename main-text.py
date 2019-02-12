from bj import Blackjack

class TextInterface:
    def __init__(self):
        print("\n     #####   BLACKJACK   #####\n")
        print("Your initial balance is $100.")

    def showPlayerCard(self, nr_of_cards, card):
        print(50*" ", card)

    def showDealerCard(self, nr_of_cards, card):
        print(30*" ", card)

    def playGame(self):
        choice = input("Would you like to try a game? ")
        if choice[0] in "yY":
            print(30*" " + " Dealer   " + 10*" " + " Player   ")
            return True
        else:
            return False
    
    def hitMe(self):
        return input("Another card(y/n): ") in "yY"
        
    def showResults(self, message, dealerPoints, playerPoints, balance):
        print("%s(dealer: %s, player: %s). Current balance: $%s\n" % (message, dealerPoints, playerPoints, balance))

    def newDeckMessage(self):
        print("\n     *****   SHUFFLEED NEW DECK   *****     \n")

if __name__ == "__main__":
    interface = TextInterface()
    BJ = Blackjack(interface)
    BJ.run()
