"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

import pandas as pd


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


calls=pd.DataFrame(calls, columns=["calling_number","receiving_number","timestamp","duration"])
max_timestamp=calls["timestamp"].max()
last_call = calls[calls["timestamp"] ==max_timestamp]

print(f'Last record of calls, {last_call["calling_number"].iloc[0]} calls {last_call["receiving_number"].iloc[0]} at time  {last_call["timestamp"].iloc[0]}, lasting  {last_call["duration"].iloc[0]} seconds')

texts=pd.DataFrame(texts, columns=["sending_number","receiving_number","timestamp"])

min_timestamp=texts["timestamp"].max()
first_text = texts[texts["timestamp"] ==min_timestamp]

print(f'First record of texts,{first_text["sending_number"].iloc[0]} calls {first_text["receiving_number"].iloc[0]} at time  {first_text["timestamp"].iloc[0]}')
