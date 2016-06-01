"""Deadpool core"""
from textblob import TextBlob
from test_deadpool import statements


def get_nouns(statement):
    """Get noun phrases for a statement"""
    return TextBlob(statement).words


def analyze(df, statement):
    """Main function"""
    nouns = get_nouns(statement)
    # check if any of the nouns are inside the data frame
    for column in df.columns:
        for noun in nouns:
            # check if column is string or not
            if isinstance(df[column].iloc[0], basestring):
                # is Metal in the value of this column
                # is Germany in the values of this column
                # and so on...
                if noun.lower() in df[column].str.lower().values:
                    print 'Number of rows in data with `{}` in column `{}` is {}'.format(
                        noun, column, len(df[df[column].str.lower() == noun.lower()])
                    )

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process a file against a query')
    parser.add_argument('-i', '--input', help='Pass an input file.', required=True)
    args = parser.parse_args()

    import pandas as pd
    df = pd.read_csv(args.input, encoding='utf-8')

    statement = raw_input('\nEnter a statement: ')
    analyze(df, statement)
