surname = input("მირიანაშვილი: ")
choice = input("გსურს გვარის შემობრუნება? (yes/no): ")

if choice == "yes":
    print(surname[::-1])
elif choice == "no":
    print(surname)
else:
    print("incorrect input")