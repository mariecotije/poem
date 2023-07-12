# Create a simple CLI Python program (using argparse), which will receive
# input_file argument and an output_file arguments.
# The Python code should read the input_file, perform some kind of operation
# on the text content of the file and write the new content to the output_file.

import argparse

parser = argparse.ArgumentParser(description='File Reader/Writer')
parser.add_argument('-i', '--input-file', default=None, help='Input file to read', required=True)
parser.add_argument('-o', '--output-file', default=None, help='Output file to write', required=True)
# optional command line argument
parser.add_argument('--reverse', action='store_true', help='Reverse the text')
# boolean flag parameter
parser.add_argument('--verbose', action='store_true', help='Expanded version for the user')

args = parser.parse_args()  # parse the arguments


def content_change(input_file, output_file):
    """Simple program that changes all letters to capital in a given text file and returns new file."""
    if args.verbose:
        print('The script will perform changes of the input file content')
        print('Starting the script')
    else:
        print('Starting the script')

    with open(input_file, mode='r', encoding='utf-8') as input_file:
        content = input_file.read()
        print('original text: ' + content)

    with open(output_file, mode='w', encoding='utf-8') as output_file:
        new_content = content.upper()
        print('changed to capital letters text: ' + new_content)
        if args.reverse:
            content = content[::-1]  # Reverse the content
            print('reversed text: ' + content)


content_change(args.input_file, args.output_file)

