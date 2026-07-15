numbers = [10, -5, 0, 7, -2, 0, 3]

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += num
    elif num < 0:
        negative += 1
    else:
        print("zero")

print("დადებითების ჯამი:", positive)
print("უარყოფითების რაოდენობა:", negative)