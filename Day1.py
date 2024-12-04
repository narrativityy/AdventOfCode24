# Open the file 'Day1Input.txt' in read mode
file = open('Day1Input.txt', 'r')

# Read all lines from the file into a list
txt = file.readlines()

# Initialize two empty lists to store the values from the input file
col1 = []
col2 = []
col2_freq_map = {}

# Iterate over each line in the input file
for i in range(len(txt)):
    # Remove the newline character from the end of the line and split the line into two values
    txt[i] = txt[i].replace('\n', '').split('   ')

    # Convert the values to integers and append them to the corresponding lists
    col1.append(int(txt[i][0]))
    col2.append(int(txt[i][1]))

    # Store the frequency of each value in column 2 in a dictionary
    if col2[i] in col2_freq_map:
        col2_freq_map[col2[i]] += 1
    else:
        col2_freq_map[col2[i]] = 1

# Sort the lists in ascending order
col1.sort()
col2.sort()

# Initialize a variable to store the total difference between the values in the two columns
total = 0

# Iterate over the range of the length of column 1 (assuming both columns have the same length)
for i in range(len(col1)):
    # Calculate the difference between the maximum and minimum values at the current index
    # and add it to the total
    total += max(col1[i], col2[i]) - min(col1[i], col2[i])

# Initialize a variable to store the similarity score
similarity_score = 0

# Iterate over the values in column 2
for num in col1:
    # If the value is in the frequency map, add it to the similarity score
    if num in col2_freq_map:
        # Multiply the value by the frequency of that value in column 2
        similarity_score += num * col2_freq_map[num]


# Print the total difference
print(total)

# Print the similarity score
print(similarity_score)