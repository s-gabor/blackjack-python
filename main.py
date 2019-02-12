from bj import Blackjack
from graphics import *
from button import Button


class GUIInterface:
    def __init__(self):
        self.win = win = GraphWin("Blackjack", 500, 500)
        win.setCoords(0,0,10,10)
        win.setBackground("lightblue")
        bjtext = Text(Point(5,9), "Blackjack").draw(win)
        bjtext.setStyle("bold")
        bjtext.setSize(20)
        playerText = Text(Point(1,7), "Dealer").draw(win)
        playerText.setStyle("bold")
        playerText.setSize(15)
        dealerText = Text(Point(1,4), "Player").draw(win)
        dealerText.setStyle("bold")
        dealerText.setSize(15)
        self.textBalance = Text(Point(5,1.5), "Balance\n$").draw(win)
        self.textBalance.setStyle("bold")
        self.hitButton = Button(win, Point(3,1.5), 2, 1, "Hit")
        self.checkButton = Button(win, Point(7,1.5), 2, 1, "Check")
        self.playButton = Button(win, Point(1,0.5), 1, 0.5, "Play!")
        self.quitButton = Button(win, Point(9,0.5), 1, 0.5, "Quit")
        self.quitButton.activate()
        self.images = []
        self.message = Text(Point(5,2.5), "").draw(win)
        self.message.setStyle("bold")
        self.message.setSize(15)

    def showDealerCard(self, no_of_cards, card):
        rank = card.getRank()
        suit = card.getSuit()
        if rank < 10:
            rank = "0" + str(rank)
        else:
            rank = str(rank)
        fileName = "cardset/" + rank + suit + ".gif"
        img = Image(Point(2+no_of_cards, 7), fileName).draw(self.win)
        self.images.append(img)
        print("rank: ",rank,"suit: ",suit)
        print(card)

    def showPlayerCard(self, no_of_cards, card):
        rank = card.getRank()
        suit = card.getSuit()
        if rank < 10:
            rank = "0" + str(rank)
        else:
            rank = str(rank)
        fileName = "cardset/" + rank + suit + ".gif"
        img = Image(Point(2+no_of_cards, 4), fileName).draw(self.win)
        self.images.append(img)

    def playGame(self):
        self.playButton.activate()
        self.quitButton.activate()
        self.hitButton.deactivate()
        self.checkButton.deactivate()
        while True:
            p = self.win.getMouse()
            if self.playButton.clicked(p):
                self.message.setText("")
                for img in self.images:
                    img.undraw()
                return True
            if self.quitButton.clicked(p):
                self.win.close()
                return False
    
    def hitMe(self):
        self.playButton.deactivate()
        self.quitButton.deactivate()
        self.hitButton.activate()
        self.checkButton.activate()
        while True:
            p = self.win.getMouse()
            if self.hitButton.clicked(p):
                return True
            if self.checkButton.clicked(p):
                return False
        
    def showResults(self, message, dealerPoints, playerPoints, balance):
        message = "{} \n {} / {}".format(message, dealerPoints, playerPoints)
        self.message.setText(message)
        self.textBalance.setText("Balance\n$" + str(balance))        

    def newDeckMessage(self):
        self.message.setText("*****   SHUFFLEED NEW DECK   *****")
        print("\n     *****   SHUFFLEED NEW DECK   *****     \n")


if __name__ == "__main__":
    interface = GUIInterface()
    blackjack = Blackjack(interface)
    blackjack.run()
