def main():
    value = []

    while True:
        user_input = input("Enter value or press enter to stop : ")
        if user_input == "":
            break
        value.append(user_input)
    
    print(f"Here is the value: {value}")

    

# Python file to call the main() function.
if __name__ == '__main__':
    main()