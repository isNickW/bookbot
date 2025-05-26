def get_book_text(path):
    with open(path) as f:
        text = f.read()
    print(text)
    return

def get_num_words(path):
    with open(path) as f:
        text = f.read()
    words = text.split()
    num = len(words)
    return num

def get_char_count(path):
    characters = {}
    with open(path) as f:
        text = f.read()
    chars = list(text)
    for char in chars:
        key = char.lower()
        if key not in characters:
            characters[key] = 1
        else:
            characters[key] += 1
    return characters

def sort_on(dict):
    return dict["num"]

def get_report(path):
    l = []
    char_count = get_char_count(path)
    for item in char_count.items():
        if item[0].isalpha():
            d = {"char": item[0], "num": item[1]}
            l.append(d)
    l.sort(reverse=True, key=sort_on)
    return l