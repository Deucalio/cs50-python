def omitVowel(text):
    output = ""
    for letter in text:
        if ("a" == letter.lower() or "e" == letter.lower() or "i" == letter.lower() or "o" == letter.lower() or "u" == letter.lower()):
            continue
        output += letter
    return output


text = input("Input: ")
print("Output:",omitVowel(text))


