from stats import get_num_words
from stats import get_report
import sys

if len(sys.argv) == 2:
    path = sys.argv[1]
    num_words = get_num_words(path)
    report = get_report(path)

    print(f"""============ BOOKBOT ============
    Analyzing book found at {path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------""")
    for char in report:
        print(f"{char['char']}: {char['num']}")
else:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)