"""
Name: <Hayam Abdalla>
<ProgramName>.py
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")
    i = 1
    for line in in_file:
        words = line.split()
        for word in words:
            out_file.write(str(i) + " " + word + "\n")
            i += 1
    in_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")
    for line in in_file:
        words = line.split()
        wage = float(words[2])
        new_wage = wage + 1.65
        total = new_wage * int(words[3])
        out_file.write(words[0] + " " + words[1] + " " + str(total) + "\n")
    in_file.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        position = 10 - i
        acc += (position * int(isbn[i]))
    return acc


def send_message(file, friend):
    in_file = open(file, "r")
    out_file = open(friend, "w+")
    for lines in in_file:
        out_file.write(lines + "\n")


def send_secret_message(file, friend, key):
    in_file = open(file, "r")
    out_file = open(friend, "w+")
    for lines in in_file:
        out_file.write(encode(lines, key) + "\n")


def send_uncrackable_message(file, friend, pad):
    in_file = open(file, "r")
    out_file = open(friend, "w+")
    p = open(pad, "r")
    key = p.read()
    for lines in in_file:
        out_file.write(encode_better(lines, key) + "\n")


def main():
    send_uncrackable_message("safest_message.txt", "friend.txt", "pad.txt")
    number_words("Walrus.txt", "Walrus_output.txt")
    hourly_wages("hourly_wages.txt", "wages_output")
    print(calc_check_sum("0072946520"))
    send_message("message.txt", "hassan.txt")
    send_secret_message("secret_message.txt", "friend1", 3)


main()
