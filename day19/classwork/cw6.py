my_list = [10, 20, 30, 40, 50]


start = int(input("10: "))
stop = int(input("50: "))


if start < 0 or stop > len(my_list) or start > stop:
    print("incorrect index")
else:
    # slicing
    result = my_list[start:stop]
    print("სიის ნაწილი:", result)