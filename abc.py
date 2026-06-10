# A versatile Python program demonstrating core language features

def greet_user(name):
    """Function to print a personalized greeting."""
    return f"Hello, {name}! Welcome to Python programming."

def check_even_odd(number):
    """Function to check if a number is even or odd."""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# --- Main Program Execution ---
if __name__ == "__main__":
    # 1. Take text input from the user
    user_name = input("Enter your name: ")
    greeting = greet_user(user_name)
    print(greeting)
    
    # 2. Loop to handle numeric calculations safely
    while True:
        try:
            user_input = input("\nEnter an integer to check (or type 'exit' to quit): ")
            
            # Check for termination condition
            if user_input.lower() == 'exit':
                print("Thank you for using the program. Goodbye!")
                break
                
            # Convert input and process numbers
            num = int(user_input)
            result = check_even_odd(num)
            print(f"The number {num} is {result}.")
            
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")
