import os
import csv

# Get the directory of the currently executing script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the CSV file
csv_path = os.path.join(current_dir, "resources", "budget_data.csv")

# Initialize variables to store the required values
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_changes = []
dates = []

# Read the CSV file and calculate the required values
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment the total number of months
        total_months += 1

        # Extract the date and profit/loss value from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the net total profit/loss
        net_total += profit_loss

        # Calculate the changes in profit/loss and store them in a list
        if total_months > 1:
            profit_change = profit_loss - previous_profit_loss
            profit_changes.append(profit_change)
            dates.append(date)

        # Update the previous profit/loss value for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_changes) / len(profit_changes)

# Find the greatest increase and decrease in profit/loss
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Find the corresponding dates for the greatest increase and decrease
increase_date = dates[profit_changes.index(greatest_increase)]
decrease_date = dates[profit_changes.index(greatest_decrease)]

# Prepare the analysis output
analysis_output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n"
)

# Define the path to the analysis text file
analysis_file_path = os.path.join(current_dir, "Analysis", "financial_analysis.txt")

# Export the results to the analysis text file
with open(analysis_file_path, "w") as analysis_file:
    analysis_file.write(analysis_output)

# Print the results to the console
print(analysis_output)
