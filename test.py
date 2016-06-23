"""Deadpool core"""
from textblob import TextBlob
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import itertools

def get_words(statement):
    """ Get all the words"""
    return TextBlob(statement).words

def stopwords_filter(statement):
    """ Removing stopwords"""
    stop_words = set(stopwords.words("english"))
    words = get_words(statement)
    filtered_words = []
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)

    return filtered_words


def get_proper_nouns(statement):
    """Get noun phrases for a statement"""
    tagged_sent = pos_tag(statement.split())
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
    return propernouns

def get_nouns(statement):
    """Get noun phrases for a statement"""
    return TextBlob(statement).noun_phrases

def lemmatize_words(statement):
    """Lemmatiziation process done """
    lemmatizer = WordNetLemmatizer()
    filtered_words = get_words(statement)
    lemmatize_word = []
    for w in filtered_words:
        lemmatize_word.append(lemmatizer.lemmatize(w))
    return lemmatize_word
      


def analyze(df, statement):
    """Main function"""
    nouns = get_nouns(statement)
    proper_nouns = get_proper_nouns(statement)
    final_words = lemmatize_words(statement)
    n_rows,n_cols = df.shape
    

    # Lists representing columns  comprising of  respective  words .
    col = []
    for i in range(0,n_cols):
        col.append([])
        

    # Introducing empty lists
    col_name = []
    new_col = []
    tuples = []
    tup = []

    for column in df.columns:
        for word in final_words:
            # check if column is string or not
            if isinstance(df[column].iloc[0], basestring):
                # If word lies in a particular column or not
                if word.lower() in df[column].str.lower().values:
                    col[df.columns.get_loc(column)].append(word)
    
    # if word is same as column name or not     
    for word in final_words:      
        for i in range(0,n_cols):         
            if word.lower() == df.columns[i].lower():
                col_name.append(df.columns[i])
    
    for x in col_name:
        if df[x].dtype == int:
            col_name = []
            col_name.append(x)
        elif df[x].dtype == long:
            col_name = []
            col_name.append(x)
    # Removing empty elements from list named col
    for x in col:
        if len(x) > 0:
            new_col.append(x)

    # Getting tuples list containing tuples of key words
    for element in itertools.product(*new_col):
        tup.append(element)
        for a in tup:
            tuples.append(list(a))

    # Length of tuples list
    len_tuple = len(tuples)

    # Changing our data frame into list form

    List_data =  map(list, df.values)
 
    def Sum(sum,df,x,items,i):
        if set(items) < set(i):
            if df[x].dtype == object:
                sum = sum + 1
                                    
            elif df[x].dtype == int: 
                sum = sum + i[df.columns.get_loc(x)]

            elif df[x].dtype == long: 
                sum = sum + i[df.columns.get_loc(x)]

            elif df[x].dtype == float:
                sum = sum + i[df.columns.get_loc(x)]
        return sum
    # Main Operation on Data frame as per Satement been asked

    print tuples
    print col_name
    print final_words

    for items in tuples:
        for x in col_name:
                sum = 0
                for i in List_data:
                    for word in final_words:
                        if word.lower() == "what":
                            if set(items) < set(i):
                                if df[x].dtype == object:
                                    sum = sum + 1
                                    
                                elif df[x].dtype == int: 
                                    sum = sum + i[df.columns.get_loc(x)]

                                elif df[x].dtype == float:
                                    sum = sum + i[df.columns.get_loc(x)]

                                elif df[x].dtype == long: 
                                    sum = sum + i[df.columns.get_loc(x)]
                   

                        if word.lower() == "how":
                            if set(items) < set(i):
                                if df[x].dtype == object:
                                    sum = sum + 1
                                    
                                elif df[x].dtype == int: 
                                    sum = sum + i[df.columns.get_loc(x)]

                                elif df[x].dtype == long: 
                                    sum = sum + i[df.columns.get_loc(x)]

                                elif df[x].dtype == float:
                                    sum = sum + i[df.columns.get_loc(x)]
                if sum != 0:
                    print sum   

                        
                            



    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process a file against a query')
    parser.add_argument('-i', '--input', help='Pass an input file.', required=True)
    args = parser.parse_args()

    import pandas as pd
    df = pd.read_csv(args.input, encoding='utf-8')

    statement = raw_input('\nEnter a statement: ')
    analyze(df, statement)