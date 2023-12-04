with open('text_1', 'r') as text_input:
    string_data = text_input.read()

separated_data = string_data.splitlines()

sum = 0
for line in separated_data:
    numbers = []
    for char in line:
        try:
            num = int(char)
            if num:
                numbers.append(str(num))
        except:
            continue
    couple_number = numbers[0] + numbers[-1]
    sum += int(couple_number)
    print(sum)