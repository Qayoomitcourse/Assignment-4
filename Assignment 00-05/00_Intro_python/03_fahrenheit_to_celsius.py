def main():
    
    fahrenheit = float(input("\033[1;3m Enter tempreture in Fahrenheit:  \033[0m"))

    celsius = (fahrenheit - 32) * 5.0/9.0

    print(f"tempreture : {fahrenheit}F = {celsius}C")



if __name__ == '__main__':
    main()