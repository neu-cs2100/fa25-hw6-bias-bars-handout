"""
File: biasbarsdata.py
------------------
Add your comments here
"""

KEY_WOMEN = "W"
KEY_MEN = "M"


def read_file(filename):
    """ 
    Read data from 'full-data.txt'. Create a word_data 
    dictionary with the data found in the file. 
    Returns the newly created dictionary. 

    Input:
        filename (str): name of the file holding professor review data

    """
    pass

def convert_rating_to_index(rating):
    """
    Converts the specified numerical rating into a "bucket"
    index for the three groups of review buckets (low reviews, 
    medium reviews, and high reviews). 
    
    Assign: 
    0-2 ---> Low
    2.1-3.9 ---> Medium
    4+ ---> High
    
    Input:
        rating (float): The numerical rating associated with 
                        a review

    Output: 
        bucket_index (int): The index of the "bucket" into which 
                          the review falls
    """

    pass

def add_data_for_word(word_data, word, gender, rating):
    """
    Updates the word_data dictionary to log an occurrence of the
    specified word in a review with the given rating about a professor
    of the specified gender.

    Input:
        word_data (dictionary): dict holding word frequency data
        word (string): the word for which frequency data is being updated
        gender (string): the gender label for the specified comment in which 
                         this word was seen
        rating (float): the numerical rating of the review in which this word
                         was seen

    Example:
    
    {'good': {'W': [0, 1, 1], 'M': [0, 0, 1]}, 'bad': {'W': [0, 0, 0], 'M': [1, 0, 0]}}
    
    (The three numbers inside the square brackets represent frequencies for 
    each bucket - low, medium and high)
    """
    pass
    

def search_words(word_data, target):
    """
    Given a word_data dictionary that stores word frequency information and a target string,
    returns a list of all words in the dictionary that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        word_data (dictionary): a dictionary containing word frequency data
        target (str): a string to look for in the names contained within word_data

    Returns:
        matching_words (List[str]): a list of all words from word_data that contain
                                    the target string
                                    
    Example: searching "fun", would return both "fun" and "funny" and any other word containing "fun"
                                    
    """
    pass

def print_words(word_data):
    """"
    Given a word_data dictionary, print out all its data, one word per line.
    The words are printed in alphabetical order,
    with the corresponding frequency data displayed in order
    of associated review quality for each gender.

    This code makes use of the sorted function, which is given as input a 
    list of elements and returns a list containing the same elements sorted in
    increasing order. For strings, "increasing" order maps to alphabetical 
    ordering.

    Input:
        word_data (dictionary): a dictionary containing word frequency data organized by gender and rating quality
    """
    pass

def main():
    # (This function is provided for you)
    import sys
    args = sys.argv[1:]

    if len(args) == 0: return
    # Two command line forms
    # 1. data_file
    # 2. -search target data_file

    # Assume no search, so filename to read
    # is the first argument
    filename = args[0]

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filename = args[2]  # Update filename to skip first 2 args

    # Read in the data from the file name
    word_data = read_file(filename)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_words(word_data, target)
        for word in search_results:
            print(word)
    else:
        print_words(word_data)


if __name__ == '__main__':
    main()