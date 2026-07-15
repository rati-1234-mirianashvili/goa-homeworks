def my_join(list,symbol):
    result=""

    for i in range(len(list)):
        result += list[i]

        if i != range(len(list)):
            result += symbol
         
        return result