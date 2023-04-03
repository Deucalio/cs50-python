items = {}

while True:
    try:
        item = input().upper()
        if (item in items):
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        # sorting dict alphabetically
        sorted_items = dict(sorted(items.items()))

        for item, count in sorted_items.items():
            print(count, item)
        break
