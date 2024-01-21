import json
import string
import argparse
import os

def main(inputString):
    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"

    # Remove unnecessary characters
    inputString = inputString.translate(str.maketrans('', '', string.punctuation))
    inputString = inputString.lower()

    # Initialize variables
    output_dict = {'notaword': 1}
    space_bool = True
    temp_len = 0

    # Write to dictionary
    while space_bool:
        temp_len = len(inputString)
        space_index = inputString.find(' ')

        # Check for end of string and get word
        if space_index < 0:
            word = inputString
        else:
            word = inputString[:space_index]

        # Add word to dictionary or increment count
        if output_dict.get(word, 0) == 0:
            output_dict[word] =  1
        else:
            output_dict[word] = output_dict[word] + 1

        # Remove word from string for next loop
        space_index = space_index + 1
        inputString = inputString[space_index:]

        # Check for end of string
        if temp_len == len(inputString):
            space_bool = False

    # Remove initializing word
    del output_dict['notaword']
    
    # Write dictionary to json file
    with open('word-counts.json', 'w') as f:
        json.dump(output_dict, f, indent = 0)

    return f

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)
    