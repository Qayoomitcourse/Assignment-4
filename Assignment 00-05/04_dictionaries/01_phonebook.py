def add_phone_numbers():
    # create empty dict
    phonebook: dict = {}

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        number = input("Enter Phone Number: ")
        phonebook[name] = number
    return phonebook


def print_phonebook(phonebook):
    for name in phonebook:
         print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = add_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()
