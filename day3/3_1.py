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
for number in numbers:
    number_with_sign = False
    for symbol in symbols:
        if symbol.line_number == number.line_number - 1:
            if number.start - 1 <= symbol.id <= number.end + 1:
                number_with_sign = True

        elif number.line_number == symbol.line_number:
            if symbol.id == number.start - 1 or symbol.id == number.end + 1:
                number_with_sign = True

        elif number.line_number + 1 == symbol.line_number:
            if number.start - 1 <= symbol.id <= number.end + 1:
                number_with_sign = True

    if number_with_sign == True:
        sum_numbers += int(number.number)


print(sum_numbers)
