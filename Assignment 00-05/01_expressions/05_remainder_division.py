def main():
    dividend: int = int(input("Please enter an integer to be divided:"))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)

    print(f"The result of this division is {quotient}  with a remainder of {remainder}")
    
if __name__ == '__main__':
    main()