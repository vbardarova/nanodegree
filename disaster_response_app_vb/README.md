# Disaster Response Pipeline Project

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python process_data.py data/messages.csv data/categories.csv DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python train_classifier.py DisasterResponse.db models/classifier.pkl`

2. Run the following command to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Screenshots
This is the frontpage:
![Alt text](https://github.com/vbardarova/nanodegree/blob/master/disaster_response_app_vb/screenshot2.png?raw=true "Screenshot2")

By inputting a word, you can check its category:
![Alt text](https://github.com/vbardarova/nanodegree/blob/master/disaster_response_app_vb/screenshot1.png?raw=true "Screenshot1")


## Content
Files:

- ML Pipeline Preparation.ipynb # ML exploration
- run.py  """Flask file that runs app"""
- process_data.py
- train_classifier.py

- app
| - template
| |- master.html  """ main page of web app"""
| |- go.html  """classification result page of web app"""

- data
|- categories.csv  """ data to process """
|- messages.csv  """ data to process """
|- ETL Pipeline Preparation.ipynb # etl exploration
- models

- notebooks

- README.md


## Required packages
flask
joblib
jupyter 
pandas
plot.ly
numpy
scikit-learn
sqlalchemy



## About
This project was prepared as part of the Udacity Data Scientist nanodegree programme. The data was provided by Figure Eight. 
