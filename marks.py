#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: December 2019
# This program calculates the average of marks inputted by the user


def calculate(list_of_marks):
    # This function calculates the average of the user's marks

    # Variables
    mark_average = 0

    # Process
    for counter in list_of_marks:
        mark_average = mark_average + counter

    mark_average = mark_average/len(list_of_marks)

    # Output
    return mark_average


def main():
    # This function outputs the average of marks inputted by the user

    # Variables
    mark_list = []
    mark = None

    # Input
    print("Enter all your marks here. When you are done, enter -1.")

    mark = int(input("Enter your mark: "))
    mark_list.append(mark)
    while mark != -1:
        mark = int(input("Enter your mark: "))
        mark_list.append(mark)

    # Process
    mark_list.pop()
    average = calculate(mark_list)

    # Output
    print("")
    print("Your average is {0}%".format(average))


if __name__ == "__main__":
    main()
