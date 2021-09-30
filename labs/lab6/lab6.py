"""
Name: <Hayam Abdalla>
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("please enter the first and last name? ")
    name = name.split(" ")
    print(name[1] + "," + name[0])


def company_name():
    company = input("please enter a three-part internet domain name?")
    company_name = company.split(".")
    print(company_name[1] + ".")


def initials():
    students = eval(input("how many student in the class?"))
    for i in range(students):
        first = input("please enter the student first name:")
        last = input("please enter the student last name:")
        print(first + "'s initials are " + "" + first[0] + last[0] + ".")


def names():
    list = input("please enter the list of names, separated by commas")
    names = list.split(",")
    for name in names:
        name = name.split(" ")

    print(name[0][0]+ name[1][0], end=" ")


def thirds():
    sentences = eval(input("how many sentences will be input?"))
    for _ in range(sentences):
        s = input("enter the sentence")
        print(s[2: len(s): 3])


def word_average():
    x = input(" enter the sentence ")
    acc = 0
    words = x.split(" ")
    for word in words:
        acc = acc + len(word)
    print(acc/len(words))


def pig_latin():
    x = input("enter the sentence")
    x = x.lower()
    words = x.split(" ")
    for word in words:
        print(word[1:]+word[0] + "ay", end=" ")


def main():
    # name_reverse()
    # company_name()
    # initials()
    # thirds()
    # pig_latin()
    word_average()
    # add other function calls here


main()
