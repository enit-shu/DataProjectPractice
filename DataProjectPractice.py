# Data Project Practice
# by Christine Shungu

import csv
import statistics

# Function to print stats to screen
# spaces to format output
def stats_output(fall, spring):
    space3 = "    "
    space2 = "   "
    space1 = "  "
    print(space3, space3, "Fall 2026", "Spring 2026")
    print("Mean  ", space1, round(statistics.mean(fall), 2), space2, round(statistics.mean(spring), 2))
    print("Median", space1, round(statistics.median(fall), 2), space3, round(statistics.median(spring), 2))
    print("STD   ", space1, round(statistics.stdev(fall), 2), space3, round(statistics.stdev(spring), 2))

# function uses csv library to parse input data file
def parse_data(csv_reader):
    fall_sem = []  # list of  fall semester grades
    spring_sem = []  # list of spring semester grades
    for line in csv_reader:
        if line[1] == 'Spring 2016':        # append grade to sping list record contains spring 2016
            spring_sem.append(int(line[2]))
        else:
            fall_sem.append(int(line[2]))   # append grade to fall list if record does not contain spring
    return(fall_sem,spring_sem)

#
with open('sample_grades.csv', 'r') as csv_data_in:
    csv_reader = csv.reader(csv_data_in)
    fall,spring = parse_data(csv_reader)

stats_output(fall, spring)
