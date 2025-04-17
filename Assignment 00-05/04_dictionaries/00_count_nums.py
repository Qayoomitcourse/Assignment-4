def get_user_number():
    user_number = []

    while True:
        user_input = (input("\033[94m Enter a value or press Enter to stop: \033[0m"))
        
        if user_input == "":
            break
        num = int(user_input)
    
        user_number.append(num)
    return user_number

def cont_nums(num_lst):
    num_dictionary = {}
    for num in num_lst:
        if num not in num_dictionary:
            num_dictionary[num] = 1
        else:
            num_dictionary[num] += 1
    return num_dictionary

def print_count(num_dictionary):
    for num in num_dictionary:
        print(f"{num} appears {num_dictionary[num]} times")

def main():
    user_number = get_user_number()
    num_dictionary = cont_nums(user_number)
    print_count(num_dictionary)


# Python boilerplate.
if __name__ == '__main__':
    main()