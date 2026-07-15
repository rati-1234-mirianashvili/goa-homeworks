# დაწერე ფუნქცია, რომელიც დააბრუნებს მხოლოდ ლუწ რიცხვებს ახალი list-ის სახით

def even_list(list):
    evens=[]

    for i in list:
        if i%2==0:
            evens.append(i)
    return evens