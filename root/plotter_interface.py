from abc import ABC, abstractmethod

class PlotterInterface(ABC):
    """Interface for plotting functionality."""
    
    @abstractmethod
    def plot_women_words(self, word_data: dict, word: str, max_frequency: int) -> None:
        """
        Plot word frequency data for women professors.
        
        Args:
            word_data (dict): Dictionary containing word frequency data
            word (str): The word to plot
            max_frequency (int): Maximum frequency for y-axis scaling
        """
        pass
    
    @abstractmethod
    def plot_man_words(self, word_data: dict, word: str, max_frequency: int) -> None:
        """
        Plot word frequency data for male professors.
        
        Args:
            word_data (dict): Dictionary containing word frequency data
            word (str): The word to plot
            max_frequency (int): Maximum frequency for y-axis scaling
        """
        pass