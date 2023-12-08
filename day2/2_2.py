import re
from itertools import groupby
import math

with open('text_2', 'r') as text_input:
    string_data = text_input.read()

separated_data = string_data.splitlines()


class Color:
    def __init__(self, number, color):
        self.number = number
        self.color = color
    def __repr__(self):
        return f'(color: {self.color}, number: {self.number})'

class Game:
    def __init__(self, id, cubs):
        self.id = id
        self.cubs = cubs

    def __repr__(self):
        return f'(id: {self.id}, cubes: {self.cubs})'


list_dict_games = []
game_number = 0
games = []
for line in separated_data:
    game_number += 1
    games_grabs = line[line.rfind(':') + 2:]
    # print(games_grabs)
    grabs = list(re.split(r'[;,]', games_grabs))
    cubs = []
    for g in grabs:
        gs = g.strip().split(' ')
        color = Color(int(gs[0]), gs[1])
        cubs.append(color)
    game = Game(game_number, cubs)
    games.append(game)


sum_of_powers = 0
for game in games:
    sorted_input = sorted(game.cubs, key=lambda c: c.color)
    groups = groupby(sorted_input, key=lambda c: c.color)

    dicts_with_colors_for_game = [{'color': c, 'items': [x.number for x in colors]} for c, colors in groups]

    list_max_colors = []
    for color_with_numbers in dicts_with_colors_for_game:
        max_number = max(color_with_numbers["items"])
        max_color = Color(max_number, color_with_numbers["color"])
        list_max_colors.append(max_color)

    num = []
    for col in list_max_colors:
        num.append(col.number)
    power_of_game = math.prod(num)
    sum_of_powers +=power_of_game
    print(sum_of_powers)




