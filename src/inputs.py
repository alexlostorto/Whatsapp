def integerInput(array, question):
    userInput = input(question)

    while True:
        # Check input is acceptable
        if userInput == '':
            print()
            return False
        elif not userInput.isdigit() or int(userInput) < 1 or int(userInput) > len(array):
            print(f"Input has to be a number 1-{len(array)}\n")
            userInput = input(question)
            continue
        else:
            print()
            return int(userInput)


def yesNo(question):
    userInput = input(question)

    while True:
        # Check input is acceptable
        if userInput == '':
            print(f"Don't leave me empty!\n")
        elif userInput.lower() in ['y', 'ye', 'yes', 'yeah']:
            print()
            return True
        elif userInput.lower() in ['n', 'no', 'nop', 'nope']:
            print()
            return False
        else:
            print(f"Write yes or no.\n")

        userInput = input(question)


def chooseFile(files):
    for i in range(len(files)):
        print(f"{i+1}) {files[i][1]}")

    file = integerInput(files, "Choose which file you want to use: ")
    print(f"You chose '{files[file-1][1]}'\n")

    return file


def chooseFunction():
    functions = [
        "displayDays",
        "textCounter"
    ]

    parameters = []

    for i in range(len(functions)):
        parameters.append(yesNo(f"Do you want to use {functions[i]}: "))

    return parameters
