def read_file(filename):
  with open(filename, 'r') as f:
    return f.read()
  
def is_valid_command(command):
    if (command[0:3] != 'mul'):
        return False
    if (command[4] != '(' and command[-1] != ')'):
        return False
    parameter = command[4:-1].split(',')
    if len(parameter) != 2:
        return False

    if not parameter[0].isnumeric() or not parameter[1].isnumeric():
        return False

    return int(parameter[0]) * int(parameter[1])

def calculate_total(txt):
  total = 0

  for i in range(len(txt)):

    if txt[i] == 'm':

      j = i + 1

      while j < len(txt) and txt[j] != ')':

        j += 1

      if j >= i + 5:

        total += is_valid_command(txt[i:j+1])

  return total

txt = read_file('Day3Input.txt')

print(calculate_total(txt))