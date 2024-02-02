import argparse as ap

def main(array):
    # Write the compute the variance and the mean of a given list of numbers
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    sum = 0
    sum_var = 0

    for num in array:
        sum += num
    mean = sum / len(array)

    for num in array:
        var = num - mean
        var = var * var
        sum_var += var

    variance = sum_var/len(array)
    output = 'mean = ' + str(mean) + "\n" + 'variance = ' + str(variance)

    print(output)

    return output

if __name__ == "__main__":
    argParse = ap.ArgumentParser("Variance and Mean Calculator")
    argParse.add_argument("--array", nargs="+", type=int, help="Input a list of numbers to compute the variance and mean of")
    parsedArgs = argParse.parse_args()
    main(parsedArgs.array)