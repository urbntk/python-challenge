import csv
df_budget = "budget_data.csv"
total_months = 0
total_revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_decrease = ["", 9999999999999999999]
biggest_increase = ["", 0]



with open(df_budget) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        if (revenue_change > biggest_increase[1]):
            biggest_increase[0] = row["Date"]
            biggest_increase[1] = revenue_change
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {biggest_increase[0]} (${biggest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

df_analysis = "budget_analysis.txt"
with open(df_analysis, "w") as txt_file:
    txt_file.write(output)