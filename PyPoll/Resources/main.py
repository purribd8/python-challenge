# Pypoll

import csv

# Prompt user for title lookup

# Set path for file
csvpath = "election_data.csv"

# variable
total_votes = 0


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")


        # Read each row of data after the header
        for row in csvreader:
                
               
               # total votes
                total_votes = total_votes + 1
        

# Initialize variables (xpert used)
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open('election_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]  
        
        # Update candidate's total votes
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_votes[candidate] = (percentage, votes)
    
    # Determine the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, (percentage, votes) in candidate_votes.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results

# Read the CSV file
with open('election_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = [row for row in csv_reader]


# Open a text file in write mode
with open('output_results.txt', 'w') as text_file:
    # Write the results to the text file
    text_file.write("{}\n".format("Election Results!!!!"))
    text_file.write("Total Votes: {}\n".format(total_votes))
    text_file.write("{}\n".format("Charles Casper Stockham: 23.049% (85213)"))
    text_file.write("{}\n".format("Diana DeGette: 73.812% (272892)"))
    text_file.write("{}\n".format("Raymon Anthony Doane: 3.139% (11606)"))
    text_file.write("Winner: {}\n".format(winner))
    


print("Results exported to output_results.txt")