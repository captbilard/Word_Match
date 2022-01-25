import difflib

matched_word = []
match_counter = 0

with open("text1.txt", 'r') as f1:
    read_file1 = f1.read().split()

with open("text2.txt", 'r') as f2:
    read_file2 = f2.read().split()

# for char_a, char_b in zip(read_file1, read_file2):
#     if char_a == char_b:
#         matched_word.append(char_a)
#         match_counter = match_counter + 1

# print(match_counter)
# print(matched_word)

diff = difflib.HtmlDiff().make_file(read_file1,read_file2, "text1.txt","text2.txt")
path = "result3.html"
f = open(path, 'w')
f.write(diff)
f.close()
