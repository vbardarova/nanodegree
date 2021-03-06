# Disaster Response Pipeline Project

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python process_data.py data/messages.csv data/categories.csv DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python train_classifier.py data/DisasterResponse.db models/classifier.pkl`

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
- app
| - template
| |- master.html  """main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process
|- disaster_messages.csv  # data to process
|- process_data.py
|- DisasterResponse.db   # database to save clean data to

- models
|- train_classifier.py
|- disaster_model.pkl  # saved model

- notebooks
|- ETL Pipeline Preparation.ipynb # etl exploration
|- ML Pipeline Preparation.ipynb # ML exploration

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
