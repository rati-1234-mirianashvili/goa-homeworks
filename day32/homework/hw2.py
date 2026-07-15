def my_split(text,symbol):
    result = []

    for letter in text:
        if letter==symbol:
            result.append(current)
            current=""
        else:
            current+=letter
        
        result.append(current)
    
    return result