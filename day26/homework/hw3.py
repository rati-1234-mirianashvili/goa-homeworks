def is_palindrome(word):
    if word == word[::-1]:
        return "პალინდრომია"
    else:
        return "არ არის პალინდრომი"

print(is_palindrome("level"))