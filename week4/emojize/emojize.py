import emoji
text = input("Input: ").strip()
emojized = emoji.emojize(text,language="alias")
print(f"Output: {emojized}")