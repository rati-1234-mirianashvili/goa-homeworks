#)შექმენით რიცხვების სია, შემდეგ ამ სიაში დაითვალეთ მხოლოდ ლუწი რიცხვების ჯამი (გამოიყენეთ % ოპერატორი)
numbers=[5,12,3,25,7,18]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
        print("largest number is:", largest)