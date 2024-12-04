# Open the file 'Day2Input.txt' in read mode
txt = open('Day2Input.txt', 'r').readlines()

# Iterate over each line in the input file
for i in range(len(txt)):
    # Remove the newline character from the end of the line and split the line into multiple values
    txt[i] = txt[i].replace('\n', '').split(' ')

# Initialize a counter for the number of safe reports
safeReports = 0

# Iterate over each report in the input file
for report in txt:
    # Initialize flags to track whether the report is increasing and valid
    increasing = False
    valid = True

    # Iterate over each level in the report
    for level in range(len(report)):
        # If this is the first level, check if the report is increasing
        if level == 0:
            # If the current level is less than the next level, the report is increasing
            if int(report[level]) < int(report[level + 1]):
                increasing = True
            # Skip to the next iteration of the loop
            continue

        # Check if the current level is equal to the previous level
        if int(report[level]) == int(report[level - 1]):
            # If the levels are equal, the report is not valid
            valid = False
        # Check if the difference between the current and previous levels is greater than 3
        elif max(int(report[level - 1]), int(report[level])) - min(int(report[level - 1]), int(report[level])) > 3:
            # If the difference is greater than 3, the report is not valid
            valid = False
        # Check if the report is increasing and the current level is less than the previous level
        elif int(report[level]) < int(report[level - 1]) and increasing:
            # If the report is increasing and the current level is less than the previous level, the report is not valid
            valid = False
        # Check if the report is not increasing and the current level is greater than the previous level
        elif int(report[level]) > int(report[level - 1]) and not increasing:
            # If the report is not increasing and the current level is greater than the previous level, the report is not valid
            valid = False

        # If this is the last level in the report and the report is still valid, increment the safe reports counter
        if level == len(report) - 1 and valid:
            safeReports += 1

# Print the total number of safe reports
print(safeReports)