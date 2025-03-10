# 1.
import random

class Card:
    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f"{self.mast} {self.number}"

class CardsDeck:
    def __init__(self):
        self.cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))

        self.cards.append(Card('Joker', 'Black'))
        self.cards.append(Card('Joker', 'Red'))

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, card_number):
        if 1 <= card_number <= len(self.cards):
            return self.cards[card_number - 1]
        else:
            return None


deck = CardsDeck()
deck.shuffle()


card_number = int(input('Выберите карту из колоды в 54 карт: '))
card = deck.get(card_number)
print(f'Your card is: {card}')


card_number = int(input('Выберите карту из колоды в 54 карт: '))
card = deck.get(card_number)
print(f'Your card is: {card}')
