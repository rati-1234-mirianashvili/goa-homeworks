# შექმენით კოდი რომელის დაპრინტავს "adult" როცა ასაკი იქნება 18 წელზე მეტი, თუ 13 წელსა და 18 წელს შორისაა დაპრინტოს "teen", ხოლო ყველა სხვა შემთხვევაში დაპრინტოს "child"

age=int(input("Enter your age "))

if age>=18:
    print("Adult")
elif age>=13 and age<18:
    print("teen")
else:
    print("child")