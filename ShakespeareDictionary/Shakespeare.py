from string import punctuation
from pathlib import Path
import time

def main():
    """
    
    """
    counts = {}

    stopwords_file = Path("stopwords.txt")
    current_file = Path("")

    print("""
Welcome to the word analyzer. 
1) Macbeth
2) A Midsummer Night's Dream
""")

    choice = input("What would you like to plot? Enter your number choice here: ")
    if choice == 1 or "1":
        current_file = Path("Midsummer.txt")
        enumerate_words(current_file, stopwords_file, counts)
    elif choice == 2 or "2":
        current_file = Path("Macbeth.txt")
        enumerate_words(current_file, stopwords_file, counts)

def enumerate_words(file_path, stopwords_file, counts):
    with open(stopwords_file) as file:
        stopwords = {line.strip() for line in file}

    with open(file_path) as file:
        for line in file:
            for word in line.split():
                cleaned = word.lower().strip(punctuation)
                if cleaned not in stopwords:
                    counts[cleaned] = counts.get(cleaned, 0) + 1
    for word in sorted(counts, key=counts.get, reverse=True)[20]:
        print(f"{word}\t{counts[word]}")




if __name__ == "__main__":
    main()