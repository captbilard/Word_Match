import difflib


def save_to_Html(file_1, file_2, read_file1, read_file2):
    """
    Compares both files and saves the result as a
    table in a html file
    """
    diff = difflib.HtmlDiff().make_file(read_file1, read_file2, file_1, file_2)
    path = "result.html"
    f = open(path, "w")
    f.write(diff)
    f.close()
    return path


def print_to_console(read_file1, read_file2):
    """
    Compares both files, print the total number
    of matches and list of matched words to the
    console.
    """
    counter, matched_words = 0, []
    for char_a, char_b in zip(read_file1, read_file2):
        if char_a == char_b:
            matched_words.append(char_a)
            counter = counter + 1
    return counter, matched_words
