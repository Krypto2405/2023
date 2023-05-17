def calculate_square(number):
    square = number ** 2
    return square

def main():
    number = float(input("Geben Sie eine Zahl ein: "))
    result = calculate_square(number)
    print("Das Quadrat von", number, "ist", result)

if __name__ == "__main__":
    main()