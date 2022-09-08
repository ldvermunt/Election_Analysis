# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

# Add our dependencies.

import csv
from distutils import text_file

import os

# Assign a variable to load a file from a path.

file_to_load = os.path.join("election_results.csv")

# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("election_analysis.txt")


# open the election results and read the file

with open(file_to_load,"r") as election_data:

    # read and analyse the data here
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

