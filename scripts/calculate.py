import sys

numbers = [0, 1]
for i in range(2, int(sys.argv[1])):
    numbers.append(numbers[i - 1] + numbers[i - 2])

with open('./data/numbers.txt', 'w') as numbers_file:
    for number in numbers:
        numbers_file.write('{}\n'.format(number))
