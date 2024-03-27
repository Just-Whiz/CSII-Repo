from string import punctuation
import time

def main():
    """
    This is the main function of the 


    """

    counted_dictionary = ""
    try:
        print("""Here are your choices for graphing the word usage in Shakespeare:
    1): Macbeth
    2): A Midsummer Night's Dream
            """)
        choice = input(int("What is your choice? "))
        if choice == 1 or "1":
            current_path = "Macbeth.txt"
            print("You are doing a Midsummer Night's Dream")
            with open(current_path):
                counted_dictionary = count_words(current_path)
                print(counted_dictionary)
        elif choice == 2 or "2": 
            current_path = "Midsummer.txt"
            print("You are doing A Midsummer Night's Dream")
            with open("current_path"):
                print(f"You are doing A Midsummer Night's Dream")
                counted_dictionary = count_words(counted_dictionary)
    except ValueError:
        print("Please enter a number value.")
        time.sleep(1)
                




def count_words(current_path):
    """
    
    """
    word_count = {}

    with open(current_path) as file:
        for line in file:
            for word in line.split():
                cleaned = word.lower().strip(punctuation)
                word_count[cleaned] = word_count.get(word, 0) + 1
    return word_count

if __name__ == "__main__":
    main()