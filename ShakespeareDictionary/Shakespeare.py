from string import punctuation
from pathlib import Path
from operator import itemgetter
import plotly.graph_objects as go
import time

def main():
    """
    
    """

    filtered_words = []
    filtered_word_values = []

    print("""
    Welcome to the word analyzer. Your choices are:
    1) Macbeth
    2) A Midsummer Night's Dream
    """)
        
    time.sleep(1)

    choice = input("What would you like to plot? Enter your number choice here: ")
    if choice == '1':
         = order_words("Macbeth")
        a = cleaned_words[0]
        b  = cleaned_words[1]
        print(a)
        print(b)
    elif choice == '2':
        order_words("Midsummer")
        
            

def order_words(file_number):

    current_dir = Path(__file__).parent
    stopwords_file = current_dir / "stopwords.txt"
    
    if file_number == "Macbeth":
        file_path = current_dir / "Macbeth.txt"
    elif file_number == "Midsummer":
        file_path = current_dir / "Midsummer.txt"

    counts = {}

    with open(stopwords_file) as file:
        stopwords = {line.strip() for line in file}

    with open(file_path) as file:
        for line in file:
            for word in line.split():
                cleaned = word.lower().strip(punctuation)
                if cleaned not in stopwords:
                    counts[cleaned] = counts.get(cleaned, 0) + 1
        ordered = dict(sorted(counts.items(), key=itemgetter(1), reverse=True)[:20])
        ordered_words = list(ordered.keys())
        ordered_values = list(ordered.values())
        return ordered_words, ordered_values

def create_pie_chart():
     labels = []
     values = []
     fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
     fig.update_layout(title="Macbeth Word Count")
     fig.show()

if __name__ == "__main__":
    main()