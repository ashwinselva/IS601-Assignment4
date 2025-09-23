from calculator import Calculator


def main():
    calc = Calculator()

    print("\nEnter two numbers:\n")
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        c = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\nChoose operation (1/2/3/4): ")
        if c not in ['1', '2', '3', '4']:
            raise ValueError("Invalid operation choice.")
        
        if c == '1':
            print(f"\nAdding {a} + {b} = {calc.add(a, b)}")
        
        elif c=='2':
            print(f"Subtracting {a} - {b} = {calc.subtract(a, b)}")
        elif c=='3':
            print(f"Multiplying {a} * {b} = {calc.multiply(a, b)}")
        elif c=='4':
            print(f"Dividing {a} / {b} = {calc.divide(a, b)}")

    except ValueError:
        print("Please enter valid numbers.")
    
    



if __name__ == "__main__":
    main()




