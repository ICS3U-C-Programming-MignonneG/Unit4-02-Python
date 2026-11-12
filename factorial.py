#!/usr/bin/env python3
# Created by: Mignonne Gihozo
# Created on: Nov 2026
# This program calculates the factorial of a number using a do-while loop.


def main():
    # this function calculates the factorial of a number using a do-while loop
    # input
    user_input = input("Enter a positive integer: ")
    print("")

    # process & output
    try:
        number = int(user_input)
        if number < 0:
            print(f"{user_input} is not a positive integer.")
        else:
            factorial = 1
            counter = 1

            # do-while loop simulation
            if number > 0:
                factorial = factorial * counter
                counter = counter + 1

            while counter <= number:
                factorial = factorial * counter
                counter = counter + 1

            print(f"{number}! = {factorial}")
    except ValueError:
        print(f"{user_input} is not a valid integer.")

    print("thank you for using the factorial calculator.")


if __name__ == "__main__":
    main()
