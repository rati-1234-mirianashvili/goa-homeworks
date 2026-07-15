numbers = [10, 20, 30, 40, 50]


fav_number = int(input("15"))


index = int(input("2: "))


if 0 <= index <= len(numbers):
    numbers.insert(index, fav_number)
    print(numbers)
else:
    print("invalid index")