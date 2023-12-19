import re

with open('text_4', 'r') as text_input:
    string_data = text_input.read()

separated_data = string_data.splitlines()

sum_of_points = 0
for line in separated_data:
    cut_line = line[line.rfind(':') + 2:]
    win_n = cut_line.split(' |')[0]
    win_numbers = list(re.findall(r'\b\d+\b', win_n))
    my_n = cut_line.split('| ')[1]
    my_numbers = list(re.findall(r'\b\d+\b', my_n))
    points = 0
    for win_number in win_numbers:
        for my_number in my_numbers:
            if win_number == my_number:
                if points == 0:
                    points += 1
                elif points >= 1:
                    points *= 2
    sum_of_points += points
print(sum_of_points)
