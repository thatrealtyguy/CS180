import argparse

def main(inputString):
    # Write the code to reverse the string here
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    output = ''

    for char in inputString[::-1]:
        output = output + char

    print(output)
    return output

if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser("String Reverser")
    argumentParser.add_argument("--string", type=str, help="Input a string to reverse")
    parsed = argumentParser.parse_args()
    main(parsed.string)