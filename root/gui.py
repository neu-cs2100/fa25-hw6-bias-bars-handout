"""
File: biasbars.py
---------------------
Bias Bars visualization using matplotlib instead of tkinter
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import TextBox
import numpy as np
import biasbarsdata


# Constants for the visualization
LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]
COLORS_WOMEN = ['#FF6B9D', '#FF8FA3', '#FFB3BA']  # Pink shades for women
COLORS_MEN = ['#4ECDC4', '#45B7B8', '#6C5CE7']    # Blue/teal shades for men
BAR_WIDTH = 0.35
FIGURE_SIZE = (12, 8)
FILENAME = "data/full-data.txt"


class BiasBarsMPL:
    def __init__(self, word_data):
        self.word_data = word_data
        self.fig, self.ax = plt.subplots(figsize=FIGURE_SIZE)
        self.fig.suptitle('Bias Bars - Word Frequency Analysis', fontsize=16, fontweight='bold')
        
        # Create text input box
        self.setup_gui()
        self.current_word = ""
        
        # Initialize with empty plot
        self.draw_empty_plot()
        
    def setup_gui(self):
        """Set up the GUI elements using matplotlib widgets"""
        # Adjust subplot to make room for text input
        plt.subplots_adjust(bottom=0.2)
        
        # Create text input box
        ax_textbox = plt.axes([0.15, 0.05, 0.3, 0.04])
        self.textbox = TextBox(ax_textbox, 'Enter word: ', initial='')
        self.textbox.on_submit(self.on_word_submit)
        
        # Create search box
        ax_search = plt.axes([0.55, 0.05, 0.3, 0.04])
        self.searchbox = TextBox(ax_search, 'Search words: ', initial='')
        self.searchbox.on_submit(self.on_search_submit)
        
        # Add instructions
        self.fig.text(0.15, 0.12, 'Enter a word above to see its frequency distribution', 
                     fontsize=10, style='italic')
        self.fig.text(0.55, 0.12, 'Search for words containing specific patterns', 
                     fontsize=10, style='italic')
        
    def draw_empty_plot(self):
        """Draw the empty plot with labels and axes"""
        self.ax.clear()
        self.ax.set_title('Enter a word to see its frequency distribution', fontsize=14)
        self.ax.set_xlabel('Review Quality Categories', fontsize=12)
        self.ax.set_ylabel('Frequency (per million words)', fontsize=12)
        
        # Set up x-axis
        x_pos = np.arange(len(LABELS))
        self.ax.set_xticks(x_pos)
        self.ax.set_xticklabels(LABELS)
        self.ax.set_xlim(-0.5, len(LABELS) - 0.5)
        
        # Add grid for better readability
        self.ax.grid(True, alpha=0.3)
        
        # Add legend
        women_patch = patches.Patch(color=COLORS_WOMEN[1], label='Women')
        men_patch = patches.Patch(color=COLORS_MEN[1], label='Men')
        self.ax.legend(handles=[women_patch, men_patch], loc='upper right')
        
        plt.draw()
    
    def on_word_submit(self, word):
        """Handle word submission"""
        word = word.strip().lower()
        if not word:
            self.show_error("Please enter a non-empty word.")
            return
        
        if " " in word:
            self.show_error("Please enter a single word with no spaces.")
            return
            
        if word not in self.word_data:
            self.show_error(f"'{word}' is not contained in the word database.")
            return
        
        self.current_word = word
        self.plot_word(word)
    
    def on_search_submit(self, search_term):
        """Handle search submission"""
        search_term = search_term.strip()
        if search_term:
            try:
                results = biasbarsdata.search_words(self.word_data, search_term)
                result_text = ' '.join(results[:20])  # Show first 20 results
                if len(results) > 20:
                    result_text += f"... (and {len(results) - 20} more)"
                print(f"Search results for '{search_term}': {result_text}")
                
                # Update the plot title to show search results
                self.ax.set_title(f"Search results for '{search_term}': {len(results)} words found", 
                                fontsize=12)
                plt.draw()
            except Exception as e:
                print(f"Search error: {e}")
    
    def show_error(self, message):
        """Display error message"""
        self.ax.clear()
        self.ax.text(0.5, 0.5, f"Error: {message}", 
                    transform=self.ax.transAxes, 
                    fontsize=14, color='red', 
                    ha='center', va='center')
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.axis('off')
        plt.draw()
    
    def plot_word(self, word):
        """Plot the frequency distribution for a given word"""
        if word not in self.word_data:
            self.show_error(f"Word '{word}' not found in database.")
            return
        
        self.ax.clear()
        
        # Get the data for this word
        gender_data = self.word_data[word]
        women_freq = gender_data[biasbarsdata.KEY_WOMEN]
        men_freq = gender_data[biasbarsdata.KEY_MEN]
        
        # Calculate positions for the bars
        x_pos = np.arange(len(LABELS))
        
        # Create the bars
        bars_women = self.ax.bar(x_pos - BAR_WIDTH/2, women_freq, BAR_WIDTH, 
                                label='Women', color=COLORS_WOMEN, alpha=0.8)
        bars_men = self.ax.bar(x_pos + BAR_WIDTH/2, men_freq, BAR_WIDTH, 
                              label='Men', color=COLORS_MEN, alpha=0.8)
        
        # Customize the plot
        self.ax.set_title(f"Frequency of '{word}' by Gender and Review Quality", 
                         fontsize=14, fontweight='bold')
        self.ax.set_xlabel('Review Quality Categories', fontsize=12)
        self.ax.set_ylabel('Frequency (per million words)', fontsize=12)
        self.ax.set_xticks(x_pos)
        self.ax.set_xticklabels(LABELS)
        
        # Add value labels on bars
        for bar in bars_women:
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{height:.1f}', ha='center', va='bottom', fontsize=9)
        
        for bar in bars_men:
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{height:.1f}', ha='center', va='bottom', fontsize=9)
        
        # Add legend
        self.ax.legend(loc='upper right')
        
        # Add grid for better readability
        self.ax.grid(True, alpha=0.3, axis='y')
        
        # Set y-axis to start from 0
        self.ax.set_ylim(0, max(max(women_freq), max(men_freq)) * 1.1)
        
        plt.draw()
    
    def show(self):
        """Display the plot"""
        plt.show()


def convert_counts_to_frequencies(word_data):
    """
    This code is provided to you! 

    It converts a dictionary 
    of word counts into a dictionary of word frequencies by 
    dividing each count for a given gender by the total number 
    of words found in reviews about professors of that gender.
    """ 
    K = 1000000
    total_words_men = sum([sum(counts[biasbarsdata.KEY_MEN]) for word, counts in word_data.items()])
    total_words_women = sum([sum(counts[biasbarsdata.KEY_WOMEN]) for word, counts in word_data.items()])
    for word in word_data:
        gender_data = word_data[word]
        for i in range(3):
            gender_data[biasbarsdata.KEY_MEN][i] *= K / total_words_men
            gender_data[biasbarsdata.KEY_WOMEN][i] *= K / total_words_women


def main():
    """Main function to run the application"""
    # Load data
    word_data = biasbarsdata.read_file(FILENAME)
    convert_counts_to_frequencies(word_data)
    
    # Create and show the matplotlib GUI
    app = BiasBarsMPL(word_data)
    app.show()


if __name__ == '__main__':
    main()