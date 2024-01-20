import json
import string
import argparse
import os

def main(inputString):
    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"
    inputString = inputString.replace(string.punctuation, '')
    inputString = inputString.lower()

    output_dict = {'notaword': 1}
    space_bool = True
    temp_len = 0

    while space_bool:
        temp_len = len(inputString)
        space_index = inputString.find(' ')
        if space_index < 0:
            word = inputString
        else:
            word = inputString[:space_index]
        if output_dict.get(word, 0) == 0:
            output_dict[word] =  1
        else:
            output_dict[word] = output_dict[word] + 1
        space_index = space_index + 1
        inputString = inputString[space_index:]
        if temp_len == len(inputString):
            space_bool = False

    del output_dict['notaword']
    return output_dict

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)
    