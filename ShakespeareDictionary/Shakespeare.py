from string import punctuation
from pathlib import Path
import csv
from time import sleep

def main():
    """

    """

    print("""Here are your choices for graphing the word usage in Shakespeare:
1): Macbeth
2): A Midsummer Night's Dream
          """)
    choice = input("What is your choice? ")
    if choice == 1 or "1":
        current_dir = Path(__file__).parent
        file_path = current_dir / "Macbeth.txt"
        dictionary = count_words(file_path)
        print(dictionary)
    elif choice == 2 or "1": 
        current_dir = Path(__file__).parent
        file_path = current_dir / "Midsummer.txt"
        print(f"You are doing Macbeth")
        count_words(file_path)




def count_words(current_path):

    word_count = {}

    with open(current_path) as file:
        for line in file:
            for word in line.split():
                cleaned = word.lower().strip(punctuation)
                word_count[cleaned] = word_count.get(word, 0) + 1
    return word_count

if __name__ == "__main__":
    main()