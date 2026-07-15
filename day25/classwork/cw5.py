#შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი და ინტეჯერი, ასევე ფუნქციას ქონდეს სია რომელშიც ჩაამატებ მომხმარებლის შემოტანილ სტრინგს იმ ინდექსზე რომელიც მან შემოიტანა

def add(str,int):
    list=["messi", "mbape", "ronaldo", "maradona"]

    if 0 <= int <= len(list):
        return(list.insert(int,str))
    else:
        print("invalid index")
    
    print(list)