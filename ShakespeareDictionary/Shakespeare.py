from string import punctuation
import time

def main():
    """
    
    """
    num_results = 20

    counts = {}

    print("""
1) Macbeth
2) Midsummer
""")
    choice = input("What would you like to plot? Enter here: ")
    if choice == "1":
        count_macbeth_words(counts, num_results, "stopwords.txt", "Macbeth.txt")
    elif choice == "2":
        count_midsummer_words(counts, num_results)

def count_macbeth_words(counts, num_results, stopwords_file, pathway):
    with open(stopwords_file) as file:
        stopwords = {line.strip() for line in file}

    with open(pathway) as file:
        for line in file:
            for word in line.split():
                cleaned = word.lower().strip(punctuation)
                if cleaned not in stopwords:
                    counts[cleaned] = counts.get(cleaned, 0) + 1
    for word in sorted(counts, key=counts.get, reverse=True)[:num_results]:
        print(f"{word}\t:{counts[word]}")



def count_midsummer_words(counts, num_results):
# feijwa
    with open("stopwords.txt") as file:
        stopwords = {line.strip() for line in file}

    with open("Midsummer.txt") as file:
        for line in file:
            for word in line.split():
                cleaned = word.lower().strip(punctuation)
                if cleaned not in stopwords:
                    counts[cleaned] = counts.get(cleaned, 0) + 1
    for word in sorted(counts, key=counts.get, reverse=True)[:num_results]:
        print(f"{word}\t:{counts[word]}")

if __name__ == "__main__":
    main()