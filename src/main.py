from calculator import Calculator


def run_calc(calc: Calculator) -> None:
    """Run one calculation using the provided Calculator instance."""
    print("\nEnter two numbers:\n")
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))

        c = input("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nChoose operation (1/2/3/4): ")
        if c not in ['1', '2', '3', '4']:
            print("Invalid operation choice.")
            return

        if c == '1':
            result = calc.add(a, b)
            op = "+"
        elif c == '2':
            result = calc.subtract(a, b)
            op = "-"
        elif c == '3':
            result = calc.multiply(a, b)
            op = "*"
        else:  # c == '4'
            try:
                result = calc.divide(a, b)
            except ValueError as e:
                print(e)
                return
            op = "/"

        print(f"\nResult: {a} {op} {b} = {result}")

    except ValueError:
        print("Please enter valid numeric values.")



def main() -> None:
    calc = Calculator()

    print("Simple calculator. Enter calculations or type 'q' at the main prompt to quit.")

    while True:
        choice = input("\nPress Enter to perform a calculation or type 'q' to quit: ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break

        run_calc(calc)


if __name__ == "__main__":
    main()




