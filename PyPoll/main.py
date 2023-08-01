import os
import csv

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
input_file = os.path.join(current_dir, "Resources", "election_data.csv")
output_file = os.path.join(current_dir, "analysis", "election_results.txt")

# Initialize variables to store election data
total_votes = 0
candidates_votes = {}
candidates_percentage = {}

# Step 1: Read the election data from the CSV file
with open(input_file, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        # Extract the voter ID, county, and candidate information from each row
        voter_id, county, candidate = row

        # Count the total number of votes cast
        total_votes += 1

        # Step 2: Calculate the number of votes each candidate received
        candidates_votes[candidate] = candidates_votes.get(candidate, 0) + 1

# Step 3: Calculate the percentage of votes each candidate won
for candidate, votes in candidates_votes.items():
    candidates_percentage[candidate] = (votes / total_votes) * 100

# Step 4: Find the winner based on popular vote
winner = max(candidates_votes, key=candidates_votes.get)

# Step 5: Print the election results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates_votes.items():
    print(f"{candidate}: {candidates_percentage[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Step 6: Export the election results to a text file
os.makedirs("analysis", exist_ok=True)  # Create the "analysis" directory if it doesn't exist
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates_votes.items():
        txtfile.write(f"{candidate}: {candidates_percentage[candidate]:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print("Analysis completed. Results have been saved to 'analysis/election_results.txt'")
