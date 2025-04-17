def get_last_element(lst):
    # Print the last element of the list
    print("The last element is:", lst[-1])


def main():
    num_elements = int(input("How many elements in the list? "))
    
    lst = []
    for i in range(num_elements):
        item = input(f"Enter element #{i + 1}: ")
        lst.append(item)
    
    get_last_element(lst)


# Python file to call the main() function.
if __name__ == '__main__':
    main()
