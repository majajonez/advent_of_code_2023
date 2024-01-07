import re

with open('text_4', 'r') as text_input:
    string_data = text_input.read()

separated_data = string_data.splitlines()


class Card:
    def __init__(self, card_number, win_numbers, my_numbers):
        self.card_number = card_number
        self.win_numbers = win_numbers
        self.my_numbers = my_numbers

    def next_cards(self):
        no_cards = 0
        won_cards = []
        for win_number in self.win_numbers:
            for my_number in self.my_numbers:
                if win_number == my_number:
                    no_cards += 1
        for i in range(no_cards):
            won_cards.append(self.card_number + i + 1)
        return won_cards

    def __repr__(self):
        return f'(card_number: {self.card_number})'


game_number = 0
cards = []
original_cards = []
for line in separated_data:
    game_number += 1
    cut_line = line[line.rfind(':') + 2:]
    win_n = cut_line.split(' |')[0]
    win_numbers = list(re.findall(r'\b\d+\b', win_n))
    my_n = cut_line.split('| ')[1]
    my_numbers = list(re.findall(r'\b\d+\b', my_n))
    card = Card(game_number, win_numbers, my_numbers)
    cards.append(card)
    original_cards.append(card)


def calc1(card):
    won_cards_idx = card.next_cards()
    won_cards = [original_cards[i - 1] for i in won_cards_idx]
    return calc(won_cards)


def calc(cards):
    cards_sum = len(cards)
    for c in cards:
        if not hasattr(c, "result"):
            wynik = calc1(c)
            c.result = wynik
            cards_sum += wynik
        else:
            global counter
            cards_sum += c.result
    return cards_sum


print(calc(cards))
