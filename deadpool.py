"""Deadpool core"""
from textblob import TextBlob
from test_deadpool import statements


def get_nouns(statement):
    """Get noun phrases for a statement"""
    return TextBlob(statement).noun_phrases


def main():
    """Main function"""
    for statement in statements:
        print get_nouns(statement)

if __name__ == '__main__':
    main()
