def load_and_clean_input(filename):
    # Open the file 'Day2Input.txt' in read mode
    txt = open('Day2Input.txt', 'r').readlines()

    # Iterate over each line in the input file
    for i in range(len(txt)):
        # Remove the newline character from the end of the line and split the line into multiple values
        txt[i] = txt[i].replace('\n', '').split(' ')

    return txt

txt = load_and_clean_input('Day2Input.txt')

# Initialize a counter for the number of safe reports
safeReports = 0

# Iterate over each report in the input file
for report in txt:
    # Initialize flags to track whether the report is increasing and mistakes
    increasing = False
    mistakes = 0

    # Iterate over each level in the report
    for level in range(len(report)):

        if mistakes > 1:
            # If the report has more than one mistake, break out of the loop
            break

        # If this is the first level, check if the report is increasing
        if level == 0:
            # If the current level is less than the next level, the report is increasing
            if int(report[level]) < int(report[level + 1]):
                increasing = True
            # Skip to the next iteration of the loop
            continue

        # Check if the current level is equal to the previous level
        if int(report[level]) == int(report[level - 1]):
            # If the levels are equal, the report is not mistakes
            mistakes += 1
        # Check if the difference between the current and previous levels is greater than 3
        elif max(int(report[level - 1]), int(report[level])) - min(int(report[level - 1]), int(report[level])) > 3:
            # If the difference is greater than 3, the report is not mistakes
            mistakes += 1
        # Check if the report is increasing and the current level is less than the previous level
        elif int(report[level]) < int(report[level - 1]) and increasing:
            # If the report is increasing and the current level is less than the previous level, the report is not mistakes
            mistakes += 1
        # Check if the report is not increasing and the current level is greater than the previous level
        elif int(report[level]) > int(report[level - 1]) and not increasing:
            # If the report is not increasing and the current level is greater than the previous level, the report is not mistakes
            mistakes += 1

        # If this is the last level in the report and the report is still mistakes, increment the safe reports counter
        if level == len(report) - 1 and mistakes < 2:
            safeReports += 1

# Print the total number of safe reports
print(safeReports)
