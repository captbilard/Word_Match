import argparse

from utilities import *

parser = argparse.ArgumentParser()
parser.add_argument("file_1", help="first text file")
parser.add_argument("file_2", help="second text file")
parser.add_argument(
    "--html",
    help="Saves the result in a table format inside an html file",
    action="store_true",
)
args = parser.parse_args()

file_1, file_2 = args.file_1, args.file_2

with open(file_1, "r") as f1:
    read_file1 = f1.read().split()

with open(file_2, "r") as f2:
    read_file2 = f2.read().split()

if args.html:
    path = save_to_Html(file_1, file_2, read_file1, read_file2)
    print(f"Comparison table saved to {path}")
else:
    counter, matched_words = print_to_console(read_file1, read_file2)
    print(f"Total count of matched words : {counter}")
    print(f"List of matched words: \n {matched_words}")
