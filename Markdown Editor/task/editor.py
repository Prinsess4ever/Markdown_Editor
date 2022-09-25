# write your code here

# Choose a formatter: > bold
# Text: > Hello
# **Hello**
# Choose a formatter: > header
# Level: > 2
# Text: > Hello World!
# **Hello**
# ## Hello World!
#
# Choose a formatter: >
all_things = ""


def plain():
    return input("Text: ")

def bold():
    text = input("Text: ")

    return f"**{text}**"

def italic():
    text = input("Text: ")

    return f"*{text}*"

def inline_code():
    text = input("Text: ")

    return f"`{text}`"

def new_line():
    return "\n"


def header():
    while True:
        level = int(input("Level: "))

        if not 1 <= level <= 6:
            print("The level should be within the range of 1 to 6")
        else:
            break

    text = input("Text: ")

    return f'\n{"#"*level} {text}\n'

def link():
    label = input("Label: ")
    url = input("URL: ")

    return f"[{label}]({url})"

def ordered_list():
    while True:
        rows = int(input("Number of rows: "))
        if rows <= 0:
            print("The number of rows should be greater than zero")
        else:
            break

    lijst = []
    string = ""

    for i in range(rows):
        row = input(f"Row #{i+1}: ")
        lijst.append(row)



    for i, word, in enumerate(lijst):
        pr = f"{i+1}. {word}"

        string += pr + '\n'



    return string

def unordered_list():
    while True:
        rows = int(input("Number of rows: "))
        if rows <= 0:
            print("The number of rows should be greater than zero")
        else:
            break

    lijst = []
    string = ""

    for i in range(rows):
        row = input(f"Row #{i+1}: ")
        lijst.append(row)




    for i, word, in enumerate(lijst):
        pr = f"*. {word}"

        string += pr + '\n'



    return string



words = {
    "plain": plain,
    "bold": bold,
    "italic": italic,
    "header": header ,
    "link" : link,
    "inline-code" : inline_code,
    "ordered-list" : ordered_list,
    "unordered-list" : unordered_list,
    "new-line" : new_line,
}

while True:
    wat = input('Choose a formatter: ')

    if wat in words:
        all_things += words[wat]()
        print(all_things.lstrip())

    elif wat == "!done":
        with open("output.md", "w") as f:
            f.write(all_things.lstrip())
        break
    elif wat == "!help":
        available = " ".join(words)
        print(f"Available formatters: {available}")
        print("Special commands: !help !done")
    else:
        print("Unknown formatting type or command")