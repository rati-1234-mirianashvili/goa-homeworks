#)შექმენით სახელების სია და მომხმარებლებს შემოატანინეთ მისი სახელი ასევე count ცვლადი, გადაუარეთ ამ სიას და რამდენჯერაც მომხმარებლის სახელი შეგხვდებათ დაპრინტე "user name" და count მოუმატე ერთი საბოლოოდ  დაპრინტე count ცვლადი
names=["luka , nika , gio , luka , ana ,luka"]
user_name=input("gio:")
count=1
for name in names:
    if name == user_name:
        count +=1
        print("user name:", user_name)
        print("count",count)