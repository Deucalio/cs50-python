def camel(text):
    s = ""
    for let in text:
        if (let.isupper()):
            s += ("_"+let.lower())
            continue
        s += let
    return s

text = input("camelCase: ")
print ("snake_case:", camel(text))
