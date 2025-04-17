def main():
    fruits = {"apple": 5, "banana": 3, "kivi": 13, "malon": 50}

    total_cast = 0
    for fruit in fruits: 
        price = fruits[fruit]
        fruits_bought = int(input(f"how many {fruit} do you want to buy? : "))
        total_cast += price * fruits_bought
    print(f"Your Total bill is Rs. {total_cast}")

if __name__ == '__main__':
    main()