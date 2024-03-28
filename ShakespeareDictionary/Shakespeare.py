from string import punctuation
import plotly.graph_objects as go
import time

def main():
    """
    
    """
    num_results = 20

    counts = {}

    current_file = input("What is your choice?")
    if current_file == 1:
        current_file = "Macbeth.txt"
    elif current_file == 2:
        current_file = "Midsummer.txt"

    with open("stopwords.txt") as file:
        stopwords = {line.strip() for line in file}

    with open(current_file) as file:
        for line in file:
            for word in line.split():
                cleaned = word.lower().strip(punctuation)
                if cleaned not in stopwords:
                    counts[cleaned] = counts.get(cleaned, 0) + 1
    for word in sorted(counts, key=counts.get, reverse=True)[:num_results]:
        print(f"{word}\t:{counts[word]}")
    

if __name__ == "__main__":
    main()