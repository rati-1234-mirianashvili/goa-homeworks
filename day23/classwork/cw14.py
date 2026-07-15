names = ["ანა", "ნიკა", "ლუკა", "მარი"]


index = 2


if 0 <= index < len(names):
    names.pop(index)
    print(names)
else:
    print("invalid index")