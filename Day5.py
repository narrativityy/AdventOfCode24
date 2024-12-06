def read_file(filename):
    with open (filename, 'r') as f:
        txt = f.readlines()
        
        for i in range(len(txt)):
            txt[i] = txt[i].replace('\n', '')
        
        return txt

def get_pair_map(txt):
    pair_map = {}

    i = 0

    while i < len(txt) and txt[i] != '':
        txt[i] = txt[i].split('|')
        print(txt[i])
        if int(txt[i][1]) in pair_map:
            pair_map[int(txt[i][1])].append(int(txt[i][0]))
        else:
            pair_map[int(txt[i][1])] = [int(txt[i][0])]
        i += 1

    return pair_map

def get_instructions(txt):
    i = 0

    while i < len(txt) and txt[i] != '':
        i += 1

    return txt[i + 1:]

txt = read_file('Day5Input.txt')
pair_map = get_pair_map(txt)
print(pair_map)
print(get_instructions(txt))