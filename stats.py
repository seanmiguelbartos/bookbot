def n_words(file_contents):
    num_words = len(file_contents.split())
    print(f"{num_words} words found in the document")
    return num_words

def n_char(file_contents):
    num_char = {}
    for i in file_contents.lower():
        if i not in num_char:
            num_char[i] = 1
        else:
            num_char[i] += 1
    print(num_char)
    return num_char

def report(file_contents):
    num_char = n_char(file_contents)
    num_words = n_words(file_contents)

    sorted_dict = sorted(num_char.items(), key = lambda x: x[1], reverse = True)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_dict:
        print(f"{char}: {count}")
    print("============= END ===============")

