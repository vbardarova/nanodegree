import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import re
import pickle
import nltk

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, make_scorer
from sklearn.model_selection import GridSearchCV

import warnings

warnings.simplefilter('ignore')

def load_data(database_filepath):
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql("SELECT * FROM Messages", engine)
    X = df['message']
    Y = df.iloc[:,4:]
    return X,Y


def tokenize(text):
    # Convert text to lowercase and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", ' ', text.lower())
    # Tokenize
    words = word_tokenize(text)
    # Remove Stopwords
    stop_words = stopwords.words("english")
    words = [w for w in words if w not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    clean = [lemmatizer.lemmatize(w, pos='n').strip() for w in words]
    clean = [lemmatizer.lemmatize(w, pos='v').strip() for w in clean]
    
    
    return clean


def build_model():
    pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer = tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    parameters = {
#     'vect__min_df': [1, 5],
#               'tfidf__use_idf':[True, False],
               'clf__estimator__n_estimators': [10,50],
              'clf__estimator__min_samples_split': [2, 4]
              }
#     scorer = make_scorer(performance_metric)
    cv = GridSearchCV(pipeline, param_grid=parameters,
#                       scoring=scorer,
                      verbose = 10)
    
    return cv
    
    

def evaluate_model(actual, predicted, col_names):
    metrics = []
    
    # Calculate evaluation metrics for each set of labels
    for i in range(actual.shape[1]):
        accuracy = accuracy_score(actual[:, i], predicted[:, i])
        precision = precision_score(actual[:, i], predicted[:, i], average="micro")
        recall = recall_score(actual[:, i], predicted[:, i], average="micro")
        f1 = f1_score(actual[:, i], predicted[:, i],average="micro")
        
        metrics.append([accuracy, precision, recall, f1])
    
    # Create dataframe containing metrics
    metrics = np.array(metrics)
    metrics_df = pd.DataFrame(data = metrics, index = col_names, columns = ['Accuracy', 'Precision', 'Recall', 'F1'])
      
    return metrics_df   

# def performance_metric(y_true, y_pred):
#     """Calculate median F1 score for all of the output classifiers
    
#     Args:
#     y_true: array. Array containing actual labels.
#     y_pred: array. Array containing predicted labels.
        
#     Returns:
#     score: float. Median F1 score for all of the output classifiers
#     """
#     f1_list = []
#     for i in range(np.shape(y_pred)[1]):
#         f1 = f1_score(np.array(y_true)[:, i], y_pred[:, i],average='micro')
#         f1_list.append(f1)
        
#     score = np.median(f1_list)
#     return score

def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,random_state = 17)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        
        Y_test_pred = model.predict(X_test)
        col_names = list(Y.columns.values)
        
        evaluate_model(np.array(Y_test), Y_test_pred, col_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()