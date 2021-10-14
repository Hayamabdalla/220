"""
Name: <Hayam Abdalla>
Partner: <your partner's name goes here – first and last>
<ProgramName>.py
"""

import math


def cash_conversion():
    x = eval(input("enter an integer: "))
    print('${:.2f}'.format(x))


def encode():
    message = input(" enter the message :")
    key = eval(input("enter the key :"))
    acc = ""
    for i in message:
        x = ord(i)
        y = x + key
        z = chr(y)
        acc += z
    print(acc)


def spherearea(radius):
    return 4 * math.pi * radius ** 2


def spherevolume(radius):
    return (4/3) * math.pi * radius ** 3


def sum_n(n):
    acc = 0
    for i in range(n):
        acc += i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc += i ** 3
    return acc


def encode_better():
    s = input("enter the message")
    k = input("enter the key")
    acc = " "
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        key = ord(key) - 97
        y = ord(c) + key
        z = chr(y)
        acc += z
    print(acc)


def main():
    cash_conversion()
    encode()
    print(spherevolume(3))
    print(spherearea(5))
    print(sum_n(7))
    print(sum_n_cubes(10))
    encode_better()


main()
