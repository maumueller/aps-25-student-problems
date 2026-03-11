#! /usr/bin/env python3
import sys

def validate_output(answer):
    output_file = sys.argv[2]
    try:
        with open(output_file, 'r') as file:
             # Read the output content
             output = file.read().strip()
             output_value = output[:-1]  # Strip off the '%'
             try:
                 answer_value = float(output_value)
             except ValueError:
                 print("Error: Output must be a valid float value followed by '%'.")
                 return False
    except FileNotFoundError:
         print(f"Error: The file '{output_file}' does not exist.")
    # Read the output content
    
    # Check if the output ends with a '%'
    if not answer.endswith('%'):
        print("Error: Output must end with a '%' symbol.")
        return False
    
    # Remove '%' and check if the remaining is a valid number
    output_value = answer[:-1]  # Strip off the '%'
    
    try:
        value = float(output_value)
    except ValueError:
        print("Error: Output must be a valid float value followed by '%'.")
        return False
    
    # Check if the value is within the valid range (0 to 100)
    if not ((answer_value - 1) < value and (answer_value + 1) > value):
        print("Error: The percentage value must be between 0 and 100.")
        return False

    print(f"Output is valid: {answer}")
    return True

def main():
    try:
        answer = str(input())
    except:
        sys.exit(43)   
    if validate_output(answer):
        sys.exit(42)
    else:
        sys.exit(43)

if __name__ == "__main__":
    main()
