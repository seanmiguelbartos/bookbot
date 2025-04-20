import sys
from stats import n_words, n_char, report

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file '{filepath}' was not found."
    except Exception as e:
        return f"An error occured: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    print(file_contents)
    n_words(file_contents)
    n_char(file_contents)
    report(file_contents)
if __name__ == "__main__":
    main()
