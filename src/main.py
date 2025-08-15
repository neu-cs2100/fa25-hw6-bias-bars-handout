import sys
from word_analyzer import WordAnalyzer

def main():
    """Main function to run the word analysis program."""
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("Usage: python main.py <word>")
        sys.exit(1)
    
    word = args[0]
    analyzer = WordAnalyzer()
    analyzer.analyze_word(word)

if __name__ == "__main__":
    main()