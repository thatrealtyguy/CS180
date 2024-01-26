import argparse
#import numpy
#import os
#import math

def main(number: int) -> int:
    # Write the code to sum up cubed numbers here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.

    if type(number) != int:
        return("Your value was not an integer. Please try again.")

    sum = 0

    for i in range(number):
        num = i*i*i
        temp_num = num

        while temp_num >= 10:
            temp_num = temp_num/10

        temp_num = int(temp_num)

        if temp_num % 2 == 0:
            sum = sum + num

    output = "cube(" + str(number) + ") = " + str(sum)
    print(output)

    return (output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    main(arguments.n)