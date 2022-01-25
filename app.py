import argparse
import difflib

parser = argparse.ArgumentParser()
parser.add_argument("file_1", help="first text file")
parser.add_argument("file_2", help="second text file")
args = parser.parse_args()

matched_word = []
match_counter = 0

file_1, file_2 = args.file_1, args.file_2

with open(file_1, 'r') as f1:
    read_file1 = f1.read().split()

with open(file_2, 'r') as f2:
    read_file2 = f2.read().split()

# for char_a, char_b in zip(read_file1, read_file2):
#     if char_a == char_b:
#         matched_word.append(char_a)
#         match_counter = match_counter + 1

# print(match_counter)
# print(matched_word)

diff = difflib.HtmlDiff().make_file(read_file1,read_file2, file_1, file_2)
path = "result3.html"
f = open(path, 'w')
f.write(diff)
f.close()
