from random import shuffle


class Card:
    """Blackjack card"""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.getRank() < 10:
            return self.rank
        else:
            return 10

    def __str__(self):
        ranks = [None, "Ace", "Two", "Three", "Four", "Five", "Six",
                 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        rankStr = ranks[self.rank]
        if self.suit == 'c':
            suitStr = "Clubs"
        elif self.suit == 'd':
            suitStr = "Diamonds"
        elif self.suit == 'h':
            suitStr = "Hearts"
        else:
            suitStr = "Spades"
        return "{0} of {1}".format(rankStr, suitStr)


class Deck:
    """Deck of 52 Balckjack cards."""
    def __init__(self):
        self.newDeck()

    def shuffle(self):
        shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop(0)

    def cardsLeft(self):
        return self.cards

    def newDeck(self):
        self.cards = []
        for rank in range(1, 14):
            for suit in "cdhs":
                self.cards.append(Card(rank, suit))


class Player:
    def __init__(self):
        self.newHand()

    def getCard(self, card):
        self.cards.append(card)
        self.val = self.val + card.value()
        if card.value() == 1:
            self.hasAce = True
        if 7 <= self.val <= 11 and self.hasAce:
            self.val = self.val + 10

    def value(self):
        return self.val

    def latestCard(self):
        return self.cards[-1]

    def countCards(self):
        return len(self.cards)

    def newHand(self):
        self.cards = []
        self.val = 0
        self.hasAce = False


class Blackjack:
    def __init__(self, interface):
        self.deck = Deck()
        self.money = 100
        self.interface = interface
        self.player = Player()
        self.dealer = Player()

    def run(self):
        self.deck.shuffle()
        while self.money >= 10 and self.interface.playGame():
            self.money = self.money - 10
            self.playRound()
            message = self.updateRound()
            self.interface.showResults(message, self.dealer.value(), self.player.value(), self.money)
            if len(self.deck.cardsLeft()) < 20:
                self.deck.newDeck()
                self.deck.shuffle()
                self.interface.newDeckMessage()
                
    def playRound(self):
        self.dealer.newHand()
        self.player.newHand()
        self.dealer.getCard(self.deck.dealCard())      #dealer gets 1 card
        self.interface.showDealerCard(self.dealer.countCards(), self.dealer.latestCard())
        self.player.getCard(self.deck.dealCard())      #player gets 2 cards
        self.interface.showPlayerCard(self.player.countCards(), self.player.latestCard())
        self.player.getCard(self.deck.dealCard())
        self.interface.showPlayerCard(self.player.countCards(), self.player.latestCard())                                
        while self.interface.hitMe():
            self.player.getCard(self.deck.dealCard())  #player gets another card
            self.interface.showPlayerCard(self.player.countCards(), self.player.latestCard())
            if self.player.value() > 21:
                break
        while self.dealer.value() < 17 and self.player.value() <= 21:
            self.dealer.getCard(self.deck.dealCard())
            self.interface.showDealerCard(self.dealer.countCards(), self.dealer.latestCard())
        
    def updateRound(self):
        p, d = self.player.value(), self.dealer.value()
        if p > 21:
            return "Player busted"
        elif d > 21:
            self.money = self.money + 20
            return "Dealer busted"
        elif p > d:
            self.money = self.money + 20
            return "Player wins"
        elif d > p:
            return "Dealer wins"
        else:
            self.money = self.money + 10
            return "It's a push"
