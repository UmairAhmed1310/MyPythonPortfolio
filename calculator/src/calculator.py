# src/calculator.py
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Run the calculator in an interactive loop."""
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'q' to quit")
    
    while True:
        try:
            user_input = input("Enter operation (e.g., 5 + 3) or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            
            # Split input into number, operator, number
            num1, op, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Use +, -, *, or /")
                continue
            
            print(f"Result: {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid input. Please use format: number operator number (e.g., 5 + 3)")

if __name__ == "__main__":
    main()