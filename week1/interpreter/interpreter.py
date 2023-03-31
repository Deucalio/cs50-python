experssion = input("Expression: ").strip().split(" ")
x, y, z = experssion
x = float(x)
z = float(z)
if (y == "+"):
    print(x+z)
elif (y == "-"):
    print(x-z)
elif (y == "*"):
    print(x*z)
elif (y == "/"):
    print(round(x/z,1))
elif (y == "**"):
    print(x**z)
else:
    print(x % z)
