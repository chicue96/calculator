import math

def pedir_numero(prompt: str):
    """It requires a number until it's valid. It accepts a comma or decimal point."""
    while True:
        s = input(prompt).strip()
        
        if s.lower() == "exit":
            return None  # permite salir también en este punto
        
        # Aceptar formato local: "3,14" -> "3.14"
        t = s.replace(",", ".")
        try:
            x = float(t)
            if math.isfinite(x): #evita inf, -inf, nan
                return x
            print("* Error: Please enter a finite number.")
        except ValueError:
            print("* Error: Please enter a valid number.")


def main():
    OPS = {
        "1": ("+", lambda a, b: a + b),
        "2": ("-", lambda a, b: a - b),
        "3": ("*", lambda a, b: a * b),
        "4": ("/", lambda a, b: a / b),
    }

    # Loop until the user decides to exit
    while True:

        print("")
        print("|==================================|")
        print("| Terminal Calculator              |")
        print("|==================================|")
        print("|                                  |")
        print("| Type the number of the operation |")
        print("| 1. Addition (+)                  |")
        print("| 2. Subtraction (-)               |")
        print("| 3. Multiplication (*)            |")
        print("| 4. Division (/)                  |")
        print("|                                  |")
        print("| Type 'exit' to quit              |")
        print("|__________________________________|")
        print("")

        input_user = input("* Enter your choice: ").strip().lower()

        if input_user == "exit":
            print("\n* Exiting the calculator. Goodbye!")
            return
        if input_user not in OPS:
            print("\n* Invalid choice. Please select a valid operation.")
            continue
        while True:
            num1 = pedir_numero("\n* Enter the first number: ")
            if num1 is None:
                print("\n* Please enter a valid number.")
                continue
            else:
                break
        while True:
            num2 = pedir_numero("* Enter the second number: ")
            if num2 is None:
                print("\n* Please enter a valid number.")
                continue
            else:
                break
        
        symbol, op = OPS[input_user]

        if symbol == "/" and num2 == 0:
            print("\n* Error: Division by zero is not allowed.")
            continue

        result = op(num1, num2)
        print(f"\n* Result:\n> {num1:g} {symbol} {num2:g} = {result:g}\n")

if __name__ == "__main__": # solo corre si ejecuto main.py directamente
    main()