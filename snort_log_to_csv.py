import re
import csv

# Define input and output file paths
log_file = "C:\\NIDS\\alert"
output_csv = "C:\\NIDS\\snort_logs.csv"

# Regular expression to extract log details
log_pattern = re.compile(r"\[\*\*\] \[.*?\] (.*?) \[\*\*\].*?(\w+)} (\d+\.\d+\.\d+\.\d+) -> (\d+\.\d+\.\d+\.\d+)")

# Open CSV file for writing
with open(output_csv, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Attack_Type", "Protocol", "Source_IP", "Destination_IP"])

    # Read and parse the log file
    with open(log_file, "r") as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                csv_writer.writerow(match.groups())

print(f"Snort logs successfully converted to {output_csv}")
