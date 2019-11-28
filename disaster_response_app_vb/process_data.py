import sys
# import libraries
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])

from sqlalchemy import create_engine

import re
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin


def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv(messages_filepath, encoding='latin-1')
    categories = pd.read_csv(categories_filepath, encoding='latin-1')
    df = messages.merge(categories, how='inner', on='id')
    return df

def clean_data(df):
    categories = df['categories'].str.split(';', expand = True)
    row = categories.iloc[0]
    category_colnames = row.transform(lambda x: x[:-2]).tolist()
    categories.columns = category_colnames
    
    for column in categories:
        categories[column] = categories[column].transform(lambda x: x[-1:])
        categories[column] = pd.to_numeric(categories[column])
    
    categories.drop('child_alone', axis = 1, inplace = True)
    df.drop('categories', axis = 1, inplace = True)
    df = pd.concat([df, categories], axis = 1)
    df.drop_duplicates(inplace = True)
    return df

def save_data(df, database_filename):
    engine = create_engine('sqlite:///'+database_filename)
    df.to_sql('Messages', engine, index=False)  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()