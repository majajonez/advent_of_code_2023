with open('text_1', 'r') as text_input:
    string_data = text_input.read()

separated_data = string_data.splitlines()

words_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def process_line(line):
    list_of_numbers = []
    counter = (-1)
    for char in line:
        counter += 1
        try:
            number = int(char)
            list_of_numbers.append(str(number))
        except:
            for word in words_numbers:
                if line.startswith(word, counter):
                    number = words_numbers.index(word)
                    list_of_numbers.append(str(number))
    result = list_of_numbers[0] + list_of_numbers[-1]
    return int(result)


sum = 0
for line in separated_data:
    line_result = process_line(line)
    sum += line_result

print(sum)