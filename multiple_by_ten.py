import sys

def multiply_by_ten(file_name):
    try:
        with open(file_name, 'r') as file:
            number = float(file.read().strip())
            multiplied = number * 10
            with open(file_name, 'w') as output_file:
                output_file.write(str(multiplied))
            print(multiplied)
    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
    except ValueError:
        print("The file does not contain a valid number.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python multiple_by_ten.py <input_file>")
    else:
        file_name = sys.argv[1]
        multiply_by_ten(file_name)