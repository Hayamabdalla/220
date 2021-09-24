"""
name: Hayam Abdalla
traffic.py

problem: Practice accumulations and nested loops

certification of authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    total_numbers_vehicles = 0
    road_numbers = eval(input("How many roads were surveyed? "))
    for i in range(road_numbers):
        total_cars = 0
        days_numbers = eval(input("how many days was road " + str(i+1) + "surveyed"))
        for day in range(days_numbers):
            cars_traveled = eval(input("how many cars traveled on day " + str(day + 1) + "?"))
            total_cars = total_cars + cars_traveled
        average_number_cars= round(total_cars/days_numbers, 2)
        print("Road" + str(i + 1) + "average vehicles per day:", average_number_cars)
        total_numbers_vehicles = total_numbers_vehicles + total_cars
    print("total number of vehicles traveled on all roads:", total_numbers_vehicles)
    average_number_vehicles = total_numbers_vehicles / road_numbers
    print("average number of vehicles per road:", round(average_number_vehicles, 2))
