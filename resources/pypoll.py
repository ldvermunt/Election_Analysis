# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("election_analysis.txt")

# 1. Initialize vote counter.
total_votes = 0

# Candidate Options & Votes
candidate_options = []

#Declare dictionary for candidates and votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""

winning_count = 0

winning_percentage = 0

# open the election results and read the file
with open(file_to_load,"r") as election_data:

    # read and analyse the data here
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    #Print each row in the csv file
    for row in file_reader:
        
        # 2. Add the total vote count
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        #If candidate does not match existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to candidates count
        candidate_votes[candidate_name] +=1

    # Save the results to that candidates count
with open(file_to_save, "w") as txt_file:

       # Print the final vote count to the terminal.
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
        # Save the final vote count to the text file.
    txt_file.write(election_results)         

    # Determne the % of votes for each candidate by looping through the counts
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

    #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

    #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) *100 

    # To do: print out each candidates name, vote count, and percentage of votes to the terminal

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f} ({votes:,})\n")

    #Print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)

    #Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine the winning vote count and candidate
    # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
    
    #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

    #and set the winning_candidate = to the candidates name
            winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to terminal.

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
#print(winning_candidate_summary.)
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)


