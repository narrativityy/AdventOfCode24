# Function to read the contents of a file
def read_file(filename):
    # Open the file in read mode and return its contents
    with open(filename, 'r') as f:
        return f.read()

# Function to validate and process multiplication commands
def is_valid_multiplication_command(command):
    # Check if the command starts with 'mul' and has the correct syntax
    if (command[0:3] != 'mul'):
        return False
    if (command[4] != '(' and command[-1] != ')'):
        return False
    
    # Extract the parameters from the command
    parameter = command[4:-1].split(',')
    
    # Check if the command has exactly two parameters
    if len(parameter) != 2:
        return False
    
    # Check if both parameters are numeric
    if not parameter[0].isnumeric() or not parameter[1].isnumeric():
        return False
    
    # If the command is valid, return the product of the parameters
    return int(parameter[0]) * int(parameter[1])

# Function to calculate the total value from the file contents
def calculate_total(txt):
    # Initialize the total value and a flag to track the processing state
    total = 0
    running = True
    
    # Iterate over each character in the file contents
    for i in range(len(txt)):
        # Check if the current character is the start of a multiplication command
        if txt[i] == 'm' and running == True:
            # Find the end of the multiplication command
            j = i + 1
            while j < len(txt) and txt[j] != ')':
                j += 1
            
            # If the command is long enough, process it and add the result to the total
            if j >= i + 5:
                total += is_valid_multiplication_command(txt[i:j+1])
        
        # Check for 'do' and 'don't' commands to update the processing state
        if (i + 4 < len(txt) and txt[i:i + 2] == 'do' and txt[i + 2:i + 4] == '()'):
            running = True
        if (i + 7 < len(txt) and txt[i:i + 5] == "don't" and txt[i + 5:i + 7] == '()'):
            running = False
    
    # Return the calculated total value
    return total

# Read the contents of the input file
txt = read_file('Day3Input.txt')

# Calculate and print the total value
print(calculate_total(txt))