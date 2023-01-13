def first_repeated_word(string):
    '''This function works by splitting the input string into a list of words, and then iterating through the list.
    For each word, it checks if it has already been seen by checking if it is in the seen_words set. 
    If it has been seen, the function returns it. 
    If the end of the list is reached without finding a repeated word, the function returns "no repetition"'''
    # Split the string into a list of words
    words = string.split()

    # Create a set to store the words we have seen
    seen_words = set()

    # Iterate through the list of words
    for word in words:
        # If the word has already been seen, return it
        if word in seen_words:
            return word
        # Otherwise, add it to the set of seen words
        seen_words.add(word)

    # If no repeated words are found, return "no repetition"
    return "no repetition"
