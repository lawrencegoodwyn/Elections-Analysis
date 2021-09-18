#The data we need to retrieve


# Assign a variable for the file to load and the path.

file_to_load = '/Users/tylergoodwyn/Desktop/Analysis Projects/election-analysis/Resources/election_results.csv'

# Open the election results and read the file.

with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = '/Users/tylergoodwyn/Desktop/Analysis Projects/election-analysis/analysis/election_analysis.txt'

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")

#Write some data to the file.
outfile.write("Hello World")

#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Close the file.
election_data.close()
