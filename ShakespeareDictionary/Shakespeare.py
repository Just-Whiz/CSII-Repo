# Program Name: 
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 2/4/24
# I pledge my honor
# Challenges: Use Plotly

from string import punctuation
from pathlib import Path
from operator import itemgetter
import plotly.graph_objects as go
import time
import sys

def main():
    """
    This is the main function of the program. It executes some other functions 
    """

    print1by1("""
Welcome to the word analyzer. Your for analyzation choices are:
    1) Macbeth
    2) A Midsummer Night's Dream
What would you like to analyze?
    """)
    time.sleep(1)

    # Prompts the user with a choice
    print1by1(">>>Enter your number choice here: ")
    choice = input("")
    if choice == '1':
        # Calls the pie chart function to create 
        create_pie_chart(1)
    elif choice == '2':
        create_pie_chart(2)
        

def create_pie_chart(choice):
    if choice == 1:
        file_name = "Macbeth"
        ordered = order_words("Macbeth")
    elif choice == 2:
        file_name = "A Midsummer Night's Dream"
        ordered = order_words("Midsummer")
    cleaned_words = ordered[0]
    cleaned_values  = ordered[1]

    labels = cleaned_words
    values = cleaned_values
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title="Word Count for " + file_name)
    fig.show()


def order_words(file_name):
    current_dir = Path(__file__).parent
    stopwords_file = current_dir / "stopwords.txt"
    
    if file_name == "Macbeth":
        file_path = current_dir / "Macbeth.txt"
    elif file_name == "Midsummer":
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


def print1by1(text, delay=0.015):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

if __name__ == "__main__":
    main()