from calculator import Calculator


def show_help() -> None:
    print("\nHelp - Available commands:")
    print("1: Perform a calculation (you will be prompted for numbers and an operation)")
    print("5: Show this help message")
    print("6: Show calculation history")
    print("7 or q: Exit the program")


def show_history(calc: Calculator) -> None:
    if not getattr(calc, "history", None):
        print("\nNo history available.")
        return
    print("\nCalculation history:")
    for i, entry in enumerate(calc.history, start=1):
        print(f"{i}. {entry}")


def perform_operation(calc: Calculator) -> None:
    """Prompt for two numbers and an operation, perform it, and record history."""
    print("\nEnter two numbers (or type 'c' to cancel):")
    try:
        raw = input("First number: ").strip()
        if raw.lower() == 'c':
            print("Cancelled.")
            return
        a = float(raw)

        raw = input("Second number: ").strip()
        if raw.lower() == 'c':
            print("Cancelled.")
            return
        b = float(raw)

        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Help\n6. History\n7. Exit")
        c = input("Choose operation (1/2/3/4) or command (5/6/7): ").strip()

        if c == '5':
            show_help()
            return
        if c == '6':
            show_history(calc)
            return
        if c in ['7', 'q']:
            print("Goodbye!")
            raise SystemExit

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

        a_f = float(a)
        b_f = float(b)
        result_f = float(result)
        entry = f"{a_f} {op} {b_f} = {result_f}"
        if not hasattr(calc, "history"):
            calc.history = []
        calc.history.append(entry)
        print(f"\nResult: {entry}")

    except ValueError:
        print("Please enter valid numeric values.")


def main() -> None:
    calc = Calculator()

    print("Simple calculator. Type a menu number to interact. Type '7' or 'q' to quit.")

    while True:
        print("\nMenu:")
        print("1) Perform calculation")
        print("5) Help")
        print("6) History")
        print("7) Exit")

        choice = input("Choose (1/5/6/7): ").strip().lower()

        if choice in ['7', 'q']:
            print("Goodbye!")
            break

        if choice == '5':
            show_help()
            continue

        if choice == '6':
            show_history(calc)
            continue

        if choice == '1' or choice == '':
            try:
                perform_operation(calc)
            except SystemExit:
                break
            continue

        print("Unknown choice. Enter 1 to calculate, 5 for help, 6 for history, 7 to exit.")


if __name__ == "__main__":
    main()




