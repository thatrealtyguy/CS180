import argparse

def main(number):
    # Write the code to determine whether or not a number is a pallindrome here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    if number < 0:
        print(False)
        return None
    
    num_str = str(number)

    if len(num_str) == 1:
        print(True)
        return None
    else:
        half_index = int(round(len(num_str) / 2))
        index = -1
        for char in num_str[:half_index]:
            end_char = num_str[index]
            if char != end_char:
                print(False)
                return None
            index -= 1

    print(True)
    return None

if __name__ == "__main__":
    arg = argparse.ArgumentParser("Pallindrome Checker")
    arg.add_argument("--x", type=int, help="Input a number to determine if it's a pallindrome")
    parsed = arg.parse_args()
    main(parsed.x)