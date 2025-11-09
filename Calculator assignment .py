# ---------- Lab 1: Python Calculator (Extended Version) ----------
# Group Name: [Group G 2nd List Students]
# Course: ICT111 - Python Programming
# ---------------------------------------------------------------

import math  # for mathematical operations

# Global variables
history = []        # to store calculation history
memory = 0.0        # to store memory values
last_result = None  # to store the last calculated result


# ---------------- BASIC ARITHMETIC FUNCTIONS ----------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is undefined.")
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

def exponent(a, b):
    return math.pow(a, b)

def square_root(a):
    if a < 0:
        print("Error: Cannot find square root of a negative number.")
        return None
    return math.sqrt(a)


# ---------------- INPUT HANDLING FUNCTION ----------------
def get_number_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# ---------------- HISTORY MANAGEMENT ----------------
def update_history(num1, operation, num2, result):
    global history
    if result is not None:
        record = f"{num1} {operation} {num2} = {result}"
        history.append(record)

def display_history():
    if not history:
        print("No history available.")
    else:
        print("\n--- Calculation History ---")
        for item in history:
            print(item)
        print("----------------------------")

def clear_history():
    global history
    history.clear()
    print("Calculation history cleared.")


# ---------------- MEMORY FUNCTIONS ----------------
def memory_add(value):
    global memory
    memory += value
    print(f"Memory updated. M = {memory}")

def memory_subtract(value):
    global memory
    memory -= value
    print(f"Memory updated. M = {memory}")

def memory_recall():
    print(f"Memory Recall: {memory}")
    return memory

def memory_clear():
    global memory
    memory = 0.0
    print("Memory cleared.")


# ---------------- MAIN PROGRAM LOOP ----------------
def main():
    global last_result
    print("Welcome to the Advanced Python Calculator!")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Modulus (%)")
        print("6. Exponent (^)")
        print("7. Square Root (√)")
        print("8. Show History")
        print("9. Clear History")
        print("10. Memory Add (M+)")
        print("11. Memory Subtract (M-)")
        print("12. Memory Recall (MR)")
        print("13. Memory Clear (MC)")
        print("14. Exit")

        choice = input("Enter choice (1-14): ")

        if choice == '14':
            print("Goodbye!")
            break
        elif choice == '8':
            display_history()
            continue
        elif choice == '9':
            clear_history()
            continue
        elif choice in ['10', '11', '12', '13']:
            if choice == '10':
                if last_result is not None:
                    memory_add(last_result)
                else:
                    print("No result in memory to add.")
            elif choice == '11':
                if last_result is not None:
                    memory_subtract(last_result)
                else:
                    print("No result in memory to subtract.")
            elif choice == '12':
                memory_recall()
            elif choice == '13':
                memory_clear()
            continue
        elif choice == '7':
            num = get_number_input("Enter number for square root: ")
            result = square_root(num)
            if result is not None:
                print(f"Result: {result}")
                update_history("√", num, "", result)
                last_result = result
            continue

        use_last = input("Use previous result? (y/n): ").lower()
        if use_last == 'y' and last_result is not None:
            num1 = last_result
            print(f"Using last result: {num1}")
        else:
            num1 = get_number_input("Enter first number: ")

        num2 = get_number_input("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        elif choice == '5':
            result = modulus(num1, num2)
            operation = '%'
        elif choice == '6':
            result = exponent(num1, num2)
            operation = '^'
        else:
            print("Invalid choice!")
            continue

        if result is not None:
            print(f"Result: {result}")
            update_history(num1, operation, num2, result)
            last_result = result


# ---------------- PROGRAM EXECUTION ----------------
if __name__ == "__main__":
    main()