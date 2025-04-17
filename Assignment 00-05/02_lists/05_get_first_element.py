def get_first_element(lst):
    print("The First element is:", lst[0])

def main():
    num_elements = int(input("How many elements in the list"))

    lst = []
    for i in range(num_elements):
        item = input(f"Enter element {i + 1}: ")
        lst.append(item)
    
    get_first_element(lst)



# Python file to call the main() function.
if __name__ == '__main__':
    main()

