def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()
    
def reverse_string(string):
    return string[::-1]
  
def calculate_total(txt):
    total = 0
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            if j - len(txt[i]) < 0 and (txt[i][j: j + 4] == 'XMAS' or reverse_string(txt[i][j: j + 4]) == 'XMAS'):
                # print(reverse_string(txt[i][j:j + 4]))
                total += 1
            if len(txt) > i + 3 and j < len(txt[i+1]) and j < len(txt[i+2]) and j < len(txt[i+3]):
                temp_txt = f'{txt[i][j]}{txt[i+1][j]}{txt[i+2][j]}{txt[i+3][j]}'
                if temp_txt == 'XMAS' or reverse_string(temp_txt) == 'XMAS':
                    print(temp_txt)
                    total += 1
            if len(txt) > i + 3 and j + 1 < len(txt[i+1]) and j + 2 < len(txt[i+2]) and j + 3 < len(txt[i+3]):
                temp_txt = f'{txt[i][j]}{txt[i+1][j+1]}{txt[i+2][j+2]}{txt[i+3][j+3]}'
                if temp_txt == 'XMAS' or reverse_string(temp_txt) == 'XMAS':
                    print(temp_txt)
                    total += 1
            if len(txt) > i + 3 and j - 1 >= 0 and j - 2 >= 0 and j - 3 >= 0:
                temp_txt = f'{txt[i][j]}{txt[i+1][j-1]}{txt[i+2][j-2]}{txt[i+3][j-3]}'
                if temp_txt == 'XMAS' or reverse_string(temp_txt) == 'XMAS':
                    print(temp_txt)
                    total += 1

    
    return total

txt = read_file('Day4Input.txt')

print(calculate_total(txt))