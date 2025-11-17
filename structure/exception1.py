# User Info and File Manager - Exception Handling Demo Project

def get_user_age():
    try:
        age = int(input("Enter your age: "))  # ValueError
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age
    except ValueError as ve:
        print("Invalid age input:", ve)
        return None

def get_list_item():
    try:
        items = ['apple', 'banana']
        index = int(input("Enter index to access fruit (0 or 1): "))
        print("You selected:", items[index])  # IndexError
    except IndexError:
        print("Index out of range.")
    except ValueError:
        print("Please enter a valid integer.")

def read_user_file():
    try:
        filename = input("Enter file name to read: ")
        with open(filename, "r") as f:
            print("File content:\n", f.read())  # FileNotFoundError
    except FileNotFoundError:
        print("File not found.")

def divide_number():
    try:
        num = int(input("Enter a number to divide 100 by: "))
        result = 100 / num  # ZeroDivisionError
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def simulate_keyerror():
    try:
        data = {"name": "Alice"}
        print("Age is:", data["age"])  # KeyError
    except KeyError:
        print("The key 'age' does not exist in dictionary.")

def simulate_typeerror():
    try:
        print("Total:", "10" + 5)  # TypeError
    except TypeError:
        print("Cannot add string and integer.")

def simulate_attributeerror():
    try:
        x = 10
        x.append(5)  # AttributeError
    except AttributeError:
        print("Integer object has no attribute 'append'.")

def simulate_importerror():
    try:
        import notamodule  # ImportError
    except ImportError:
        print("Module not found.")

def simulate_nameerror():
    try:
        print(user_name)  # NameError
    except NameError:
        print("Variable 'user_name' is not defined.")

def simulate_permissionerror():
    try:
        with open("/etc/shadow", "r") as f:  # PermissionError (Linux-specific)
            print(f.read())
    except PermissionError:
        print("Permission denied to read the file.")

def simulate_assertionerror():
    try:
        assert 2 + 2 == 5  # AssertionError
    except AssertionError:
        print("Assertion failed: 2 + 2 != 5")

def main():
    print("=== Exception Handling Demo Project ===")
    get_user_age()
    get_list_item()
    read_user_file()
    divide_number()
    simulate_keyerror()
    simulate_typeerror()
    simulate_attributeerror()
    simulate_importerror()
    simulate_nameerror()
    simulate_permissionerror()
    simulate_assertionerror()
    print("=== End of Demo ===")

if __name__ == "__main__":
    main()
