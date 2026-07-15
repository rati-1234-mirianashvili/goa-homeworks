# დაწერე ფუნქცია რომელიც იღებს სიტყვების სიას და აბრუნებს ყველაზე გრძელ სიტყვას.

def longest_word(list):
    longest = list[0]
    for i in list:
        if len(i)> len(longest):
            longest=i
    return longest