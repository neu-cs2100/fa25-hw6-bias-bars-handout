from plotter_interface import PlotterInterface
from analyzer_interface import WordAnalyzerInterface
from data_loader import DataLoader
from word_plotter import WordPlotter

class WordAnalyzer(WordAnalyzerInterface):
    """Main class that coordinates data loading and plotting."""
    
    def __init__(self, data_loader: DataLoaderInterface = None, plotter: PlotterInterface = None):
        """
        Initialize the WordAnalyzer with optional dependency injection.
        
        Args:
            data_loader (DataLoaderInterface): Optional data loader implementation
            plotter (PlotterInterface): Optional plotter implementation
        """
        # Use dependency injection pattern - allows for easy testing and extensibility
        self.data_loader = data_loader if data_loader is not None else DataLoader()
        self.plotter = plotter if plotter is not None else WordPlotter()
    
    def analyze_word(self, word: str, data_filename: str = 'word_data.json') -> None:
        """
        Analyzes a word by loading data and creating plots for both genders.
        
        Args:
            word (str): The word to analyze
            data_filename (str): Path to the JSON data file
        """
        # Load the data using the injected data loader
        # YOUR CODE HERE:
        # 1. Use self.data_loader.load_dictionary_from_json() to load the data
        # 2. Extract gender data for the word from the loaded dictionary
        # 3. Calculate maximum frequency for consistent y-axis scaling across both plots
        # 4. Call self.plotter.plot_women_words() and self.plotter.plot_man_words()
        
        pass