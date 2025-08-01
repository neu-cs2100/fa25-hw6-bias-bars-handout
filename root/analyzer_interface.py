from abc import ABC, abstractmethod

class WordAnalyzerInterface(ABC):
    """Interface for word analysis operations."""
    
    @abstractmethod
    def analyze_word(self, word: str, data_filename: str = 'word_data.json') -> None:
        """
        Analyze a word by loading data and creating visualizations.
        
        Args:
            word (str): The word to analyze
            data_filename (str): Path to the JSON data file
        """
        pass