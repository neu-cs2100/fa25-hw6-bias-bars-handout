import matplotlib.pyplot as plt
from plotter_interface import PlotterInterface

class WordPlotter(PlotterInterface):
    """Handles plotting functionality for word frequency data."""
    
    LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]
    
    def __init__(self):
        self.x_vals = [0, 1, 2]
    
    def plot_women_words(self, word_data: dict, word: str, max_frequency: int) -> None:
        """
        This function takes in the word_data dictionary, the word, and the max_frequency.
        Your job is to use the dictionary and the word to plot the frequencies for this word
        use in low, medium, and high reviews when rating women professors. You do not need to worry
        about the max_frequency parameter. That is used in the provided code.
        
        Args:
            word_data (dict): Dictionary containing word frequency data
            word (str): The word to plot
            max_frequency (int): Maximum frequency for y-axis scaling
        """
        # provided code to create a new pyplot figure
        plot1 = plt.figure(1)
        
        # YOUR CODE HERE to make a plot for the woman data for a given word
        # Hint: Extract the women's data from word_data, then use plt.bar() or plt.plot()
        # to create your visualization. Use self.x_vals for x-axis positions.
        pass
        
        # END OF YOUR CODE HERE. The code below is provided for you.
        plt.ylim((0, max_frequency + 500))  # sets the maximum y value for the plot
        plt.xticks(self.x_vals, self.LABELS)  # sets the x values to be words for each review category
    
    def plot_man_words(self, word_data: dict, word: str, max_frequency: int) -> None:
        """
        This function takes in the word_data dictionary, the word, and the max_frequency.
        Your job is to use the dictionary and the word to plot the frequencies for this word
        use in low, medium, and high reviews when rating male professors. You do not need to worry
        about the max_frequency parameter. That is used in the provided code.
        
        Args:
            word_data (dict): Dictionary containing word frequency data
            word (str): The word to plot
            max_frequency (int): Maximum frequency for y-axis scaling
        """
        # provided code to create a new pyplot figure
        plot2 = plt.figure(2)
        
        # YOUR CODE HERE to make a plot for the man data for a given word
        # Hint: Extract the men's data from word_data, then use plt.bar() or plt.plot()
        # to create your visualization. Use self.x_vals for x-axis positions.
        pass
        
        # END OF YOUR CODE HERE. The code below is provided for you. Uncomment the last line when you are ready.
        plt.ylim((0, max_frequency + 500))  # sets the maximum y value for the plot
        plt.xticks(self.x_vals, self.LABELS)  # sets the x values to be words for each review category
        plt.show()