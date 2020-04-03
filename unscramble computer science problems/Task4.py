"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

calling_numbers = {call[0] for call in calls}

receiving_numbers = {call[1] for call in calls}

texts_numbers = {(text[0],text[1]) for text in texts}
texts_numbers_list=[item for sublist in texts_numbers for item in sublist]
telemarketers= []
for call in calling_numbers:
    if call not in receiving_numbers:
        if call not in texts_numbers_list:
            telemarketers.append(call)

print(f"These numbers could be telemarketers:")
telemarketers_list = sorted(telemarketers)
for i in telemarketers_list:
    print(i)

