# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote
total_votes = 0

#2. Declare candidate variable
candidate_options=[]
#3. Declare the candidate dictionary
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    # Print each row in the csv file
    for row in file_reader:
        print(row)
        #2. Add to the total vote count
        total_votes += 1
        # Print the candidate names
        candidate_name=row[2]
        #If the candidate name does not match a previous name
        if candidate_name not in candidate_options:
            #Add it to the list
            candidate_options.append(candidate_name)
            #Begin tracking candidate's votes
            candidate_votes[candidate_name] = 0
        #Tabulate candidate's votes
        candidate_votes[candidate_name] += 1
    # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

#3. Print the candidate dictionary
print(candidate_votes)
