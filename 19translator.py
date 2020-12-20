def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a Phrase : ")))
print("-------------------------------")
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":       # converts all to lower for validation
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a Phrase : ")))
print("-------------------------------")
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():        # But Capital letters will be replaced by Capital G.
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a Phrase : ")))

