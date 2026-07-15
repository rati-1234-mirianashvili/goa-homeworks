surname= input("mirianashvili")
case=input(surname.upper())


if case == "upper" :
    print(surname.upper)


elif case =="lower" :
    print(surname.lower())
     

elif case == "capitalze" :
    print(surname.capitalize)

elif case == "none" :
    print(surname)

else:
    print("incorrect input")