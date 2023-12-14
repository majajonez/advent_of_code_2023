import re

with open('text_3', 'r') as text_input:
    string_data = text_input.read()

separated_data = string_data.splitlines()

class Symbol:
    def __init__(self, value, id, line_number):
        self.value = value
        self.id = id
        self.line_number = line_number

    def __repr__(self):
        return f'(value: {self.value}, id: {self.id}, line_number: {self.line_number})'


class Number:
    def __init__(self, number, start, end, line_number):
        self.number = number
        self.start = start
        self.end = end
        self.line_number = line_number

    def __repr__(self):
        return f'(number: {self.number}, start: {self.start}, end: {self.end}, line_number: {self.line_number})'

line_number = 1
symbols = []
numbers = []
for line in separated_data:
    signs = list(re.finditer(r'[^.\d]', line))
    for s in signs:
        id = s.start()
        value = line[id]
        sign = Symbol(value, id, line_number)
        symbols.append(sign)

    num = list(re.finditer(r'\b\d+\b', line))
    for n in num:
        start_id = n.start()
        end_id = n.end() - 1
        value = line[start_id:end_id + 1]
        number = Number(value, start_id,end_id, line_number)
        numbers.append(number)
    line_number += 1

sum_numbers = 0

for symbol in symbols:
    couple_numbers = []
    for number in numbers:
        if symbol.value == '*':
            if symbol.line_number -1 == number.line_number:
                if number.start - 1 <= symbol.id <= number.end + 1:
                    couple_numbers.append(int(number.number))
            elif symbol.line_number == number.line_number:
                if symbol.id == number.start - 1 or symbol.id == number.end + 1:
                    couple_numbers.append(int(number.number))
            elif symbol.line_number +1 == number.line_number:
                if number.start - 1 <= symbol.id <= number.end + 1:
                    couple_numbers.append(int(number.number))
    if len(couple_numbers) == 2:
        multiplication = couple_numbers[0] * couple_numbers[1]
        sum_numbers += multiplication

print(sum_numbers)