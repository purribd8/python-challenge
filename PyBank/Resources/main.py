# Pybank
import csv

# Set path for file
csvpath = "budget_data.csv"

# month count variable
month_count = 0
total_profit = 0

# changes
last_month_profit = 0
changes = []
month_changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)

    # Print header
    print(f"CSV Header: {csv_header}")
    
    # loop
    for row in csvreader: 
        
        # add profit
        total_profit = total_profit + int(row[1])

        # count months
        month_count = month_count + 1 

        # need last month profits
        # subtract this month profit - last month profit
        # append change to list

        # first row calculation
        if (month_count == 1):
            # this is the first row
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            # reset last month profit
            last_month_profit = int(row[1])

    print("Financial Analysis")
    print("-------------------------")


    print(f"Total Months: {month_count}")
    print(f"Total Profit: {total_profit}")
    

    avg_change = sum(changes) / len(changes)
    rounded_number= round(avg_change,2) # Round to 2 decimal places
    print(f"Average Change: {rounded_number}")


    # Initialize variables
max_increase = 0
max_increase_date = ""

# Load the data from the CSV file
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)
    
    # Initialize variables to store previous profit
    prev_profit = 0
    
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        
        # Calculate the profit change
        profit_change = profit - prev_profit
        
        # Update the maximum increase if the current change is greater
        if profit_change > max_increase:
            max_increase = profit_change
            max_increase_date = date
        
        # Update the previous profit for the next iteration
        prev_profit = profit

# Print the result
print(f"Greatest increase in Profits: {max_increase_date} (${max_increase})")

# Initialize variables
greatest_decrease = 0
greatest_decrease_month = ""
previous_profit = 0

# Read the CSV file
with open('budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        profit = int(row[1])
        if previous_profit != 0:
            profit_change = profit - previous_profit
            if profit_change < greatest_decrease:
                greatest_decrease = profit_change
                greatest_decrease_month = row[0]
        previous_profit = profit

print(f"Greatest decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export results (xpert used)

# Read the CSV file
with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = [row for row in csv_reader]


# Open a text file in write mode
with open('output_results.txt', 'w') as text_file:
    # Write the results to the text file (reformatted some of this)
    text_file.write("{}\n".format("Financial Analysis"))
    text_file.write("Total Months: {}\n".format(month_count))
    text_file.write("Total: {}\n".format(total_profit))
    text_file.write("Average Change: {}\n".format(rounded_number))
    text_file.write("Greatest Increase in Profits: {} (${})\n".format(max_increase_date, max_increase))
    text_file.write("Greatest Decrease in Profits: {} (${})".format(greatest_decrease_month, greatest_decrease))
   

    # Print txt file
print("Results exported to output_results.txt")





