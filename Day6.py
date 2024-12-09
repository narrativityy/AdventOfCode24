def open_file(file_name):
  with open(file_name, 'r') as f:
    txt = f.readlines()
    return [line.strip() for line in txt]
  
def find_guard(txt):
  for i in range(len(txt)):
    for j in range(len(txt[i])):
      if txt[i][j] == '^':
        return [i, j]

txt = open_file('Day6Input.txt')

guard_position = find_guard(txt)

print(guard_position)
print(txt[guard_position[0]][guard_position[1]])