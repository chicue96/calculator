
def pedir_numero(prompt: str):
    """Pide un número hasta que sea válido. Acepta coma o punto decimal."""
    while True:
        s = input(prompt).strip()
        print(s)
        if s.lower() == "exit":
            return None  # permite salir también en este punto
        
        # Aceptar formato local: "3,14" -> "3.14"
        t = s.replace(",", ".")

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
            print("\nExiting the calculator. Goodbye!")
            return
        elif input_user in ["1", "2", "3", "4"]:

                num1 = pedir_numero("\n* Enter the first number: ")
                num2 = pedir_numero("* Enter the second number: ")
                
                if num1.isdigit() and num2.isdigit():
                    if input_user == "4" and num2 == "0":
                        print("\n* Error: Division by zero is not allowed.")
                    else:
                        if input_user == "1":
                            result = int(num1) + int(num2)
                            operation = "+"
                        elif input_user == "2":
                            result = int(num1) - int(num2)
                            operation = "-"
                        elif input_user == "3":
                            result = int(num1) * int(num2)
                            operation = "*"
                        elif input_user == "4":
                            result = int(num1) / int(num2)
                            operation = "/"

                        print(f"\n Result: {num1} {operation} {num2} = {result}\n")
                else:
                    print("* Error: Please enter valid numbers.")            
        else:
            print("\nInvalid choice. Please select a valid operation.")

if __name__ == "__main__": # solo corre si ejecuto main.py directamente
    main()