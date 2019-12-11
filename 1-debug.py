import ipdb


numbers = [1, 2, 3, 4, 5]
ipdb.set_trace()
for number in numbers:
    if number % 2 == 0:
        print(number)
