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
    This is the main function of the program. It executes all the other functions located in this file.
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
        # Calls the pie chart function to create a pie chart
        create_pie_chart(1)
    elif choice == '2':
        # Calls the pie chart function to create a pie chart
        create_pie_chart(2)
        

def create_pie_chart(choice):
    """
    This function creates a pie chart based on the user's choice.

    First, it asks the user for what text they want a pie chart word analysis of. It then sets the current file to be scanned
    to the user's choice, and relays that choice to another function that counts, cleans, and returns the top words found in 
    each respective document. Once that information is retrieved by this function, it is then used to create a pie chart based
    on the values returned by the file.

    """
    # If the user chooses Macbeth
    if choice == 1:
        file_name = "Macbeth"
        ordered = order_words("Macbeth")
    # If the user chooses Midsummer Night's Dream
    elif choice == 2:
        file_name = "A Midsummer Night's Dream"
        ordered = order_words("Midsummer")
    
    # Sets the "cleaned" words and numbers to values of the returned tuple values from the order_words() function
    cleaned_words = ordered[0]
    cleaned_values  = ordered[1]

    # The labels and values on the pie charts are set to the values of cleaned_words and cleaned_values, respectiely
    labels = cleaned_words
    values = cleaned_values

    # Creates a pie chart using the Figure library, and sets labels to labels, and values to values.
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    # Sets the title of the pie chart and displays the word count of the document in one's web browser
    fig.update_layout(title="Word Count for " + file_name)
    fig.show()


def order_words(file_name):
    """
    This function counts, cleans, and returns the top 10 words in a selected text.

    It retrieves the current directory by using the PATH library preinstalled by Python. It then gets the stopwords.txt file
    from the current directory and also retrieves the file to be analyzed. Then, using a dictionary, all words from the file are
    stripped of punctuation, "nonsensical" words, and then, and only then, are they counted and stored within the dictionary. After
    this process, the top 10 words are then filtered out and formatted into a dictionary that will then be later used by other functions
    in other variable processes. 
    """

    # Sets the current file path
    current_dir = Path(__file__).parent

    # Gets the "stopwords.txt" file that will be used to filter out "garbage" words and fillers
    stopwords_file = current_dir / "stopwords.txt"
    
    # Simple logic that sets the document to be scanned based on the variable argument file_name
    if file_name == "Macbeth":
        file_path = current_dir / "Macbeth.txt"
    elif file_name == "Midsummer":
        file_path = current_dir / "Midsummer.txt"

    # Creates an empty dictionary that will be used to store the counted words
    counts = {}

    # Method that opens stopwords.txt until all the code within the loop is run, where it will then close
    with open(stopwords_file) as file:
        # Strip all the "nonsense" words from the file (such as connecting words such as "the") from the current file
        stopwords = {line.strip() for line in file}

    # Method that opens the current file as a file
    with open(file_path) as file:

        # For every line and word within the file:
        for line in file:
            for word in line.split():
                # Clean up each word and strip all the punctuation (such as whitespace and commas)
                cleaned = word.lower().strip(punctuation)

                # If the previously "cleaned" words aren't in stopwords, then add them to the dictionary in the following format:
                if cleaned not in stopwords:
                    # Cleaned word, followed by its value + 1 for every instance of the word found
                    counts[cleaned] = counts.get(cleaned, 0) + 1

        # Finds the top 10 words in the dictionary, and sets this "ordered" pair to the variable ordered
        ordered = dict(sorted(counts.items(), key=itemgetter(1), reverse=True)[:20])

        # Sets the ordered_words variable to the key values (the cleaned word value) of the cleaned dictionary
        ordered_words = list(ordered.keys())
        # Sets the ordered_values variable value pairs (the # of times each word appears in each document) of the cleaned dictionary
        ordered_values = list(ordered.values())

        # Returns the cleaned values
        return ordered_words, ordered_values


def print1by1(text, delay=0.015):
    """
    This function simply prints text one by one, in rapid succession, for aesthetic purposes, in the console.

    By using the sys library preinstalled in Python, we are able to print each character of a print statement to the console,
    and then delay the subsequent display of characters by a certain delay
    """

    # For every character in the text being printed
    for c in text:
        # Write the character to the console display
        sys.stdout.write(c)
        # Remove the character from the memory
        sys.stdout.flush()
        # Wait a bit of time before printing the next character
        time.sleep(delay)
    print

if __name__ == "__main__":
    main()