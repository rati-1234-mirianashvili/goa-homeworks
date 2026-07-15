names = {"Saba", "Nika", "Giorgi", "Ana"}

user_name = input("შეიყვანეთ თქვენი სახელი: ")

if user_name in names:
    print("ეს სახელი არის სეტში და აღარ დაემატება")
else:
    names.add(user_name)
    print("სახელი დაემატა სეტში")
    print(names)

