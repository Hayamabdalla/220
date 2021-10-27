"""
name: Hayam Abdalla
weighted_average.py

problem: develop a python program that uses numeric data from a text file.
certification of authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    final = 0
    students = 0
    for line in in_file:
        # split line into pieces
        line_split = line.split(":")
        line_split = line_split[1].split()
        name = line.split(":")[0]

        # grab weights from split line
        weight = line_split[0:len(line_split):2]

        # total up the weights
        total = 0
        for i in weight:
            converted_weight = int(i)
            total = converted_weight + total

        if total == 100:
            students += 1
            # calculate a student's average
            start = 0
            acc = 0
            for i in range(0, len(line_split), 2):
                pair = line_split[start:]
                product = int(pair[0]) * int(pair[1])  # w*g
                start = start + 2
                acc += product
            # finish calculating average
            weighted_grade = acc/100
            weighted_grade_round = round(weighted_grade, 1)

            final += weighted_grade
            out_file.write(name + "'s average: " + str(weighted_grade_round) + "\n")

        else:
            # weights != 100
            if total < 100:
                out_file.write(name + "'s average" + ":" + " Error: The weights are less than 100.\n")
            else:
                out_file.write(name + "'s average" + ":" + " Error: The weights are more than 100.\n")

    final_class_average = round(final / students, 1)
    out_file.write("Class average" + ":" + " " + str(final_class_average) + "\n")


def main():
    weighted_average("grades.txt", "avg.txt")



if __name__ == '__main__':
    main()
