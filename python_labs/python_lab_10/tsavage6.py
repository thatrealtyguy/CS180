import argparse
import numpy as np

def main(documentsTxt):
    text = documentsTxt
    words = []
    # Split the string
    for word in text.split():
        words.append(word)
    # Get important values
    unique_words = list(set(words))
    unique_words.sort()
    num_words = len(unique_words)
    num_docs = text.count('\n')

    # Intialize the dictionary
    word_counts = {word: [0] * num_docs for word in unique_words}

    # For each document, make it into a string
    for i in range(num_docs):
        doc = ''
        for char in text:
            if char != "\n":
                doc += char # Add character to document string
            else:
                break

        # Trim the input text and split the document string into words
        text = text[text.find("\n") + 1:]
        words = doc.split()

        # Iterate through the words
        for word in words:
            # Find the word in the dictionary
            if word in word_counts:
                # Access the first element and increment it
                word_counts[word][i] += 1

    # Initialize output matrix
    output_matrix = [[0 for _ in range(num_docs)] for _ in range(num_words)]
    column = 0
    # Put the word counts into the matrix
    for word, count in word_counts.items():
        output_matrix[column] = count
        column += 1

    # Transpose the matrix
    output_matrix = np.transpose(output_matrix)

    print("# Features:")
    print(output_matrix)
    return(output_matrix)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())