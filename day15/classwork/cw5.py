# მომხმარებელს შემოატანინე მისი საყვარელი ფილმი და სახელი, თუ მისი სახელი ავთოა მაშინ დაპრინტე "you are avto" , თუ ლევანი ქვია და მისი საყვარელი ფილმია ტიტანიკი, დაპრინტე "Levani loves titanic" ყველა სხვა შემთხვევაში დაპრინტე "someone likes other film" (indented if-else)

movie =input("Enter your favourite movie ")
name=input("Enter your name ")

if name=="avto":
    print("you are avto")
elif name=="levani" and movie=="titanic":
    print("levani loves titanic")
else:
    print("someone likes other film")