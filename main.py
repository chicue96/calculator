
def main():

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
    print("|                                  |")
    print("|==================================|")

    input_user = input(" Enter your choice: ")

    if input_user == "exit":
        print("Exiting the calculator. Goodbye!")
        return


if __name__ == "__main__": # solo corre si ejecuto main.py directamente
    main()