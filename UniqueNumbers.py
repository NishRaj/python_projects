numbers = list()
while True:
    num = int(input("Number:"))
    if num in numbers:
        break
    numbers.append(num)
    