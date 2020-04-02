"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dictionary_calls = defaultdict(int)

for dialer, receiver, timestamp, duration in calls:
    dictionary_calls[dialer] += int(duration)
    dictionary_calls[receiver] += int(duration)

max_duration = max(dictionary_calls.items(), key=lambda x: x[1])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_duration[0], max_duration[1]))
