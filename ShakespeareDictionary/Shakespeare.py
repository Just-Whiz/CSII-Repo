from string import punctuation
from pathlib import Path
import csv

def main():
    current_dir = Path(__file__).parent
    file_path = current_dir / "Macbeth.txt"

    counts = {}

    with open(file_path) as file:
        for line in file:
            for word in line.split():
                cleaned = word.lower().strip(punctuation)
                counts[cleaned] = counts.get(word, 0) + 1

    print(counts)

if __name__ == "__main__":
    main()