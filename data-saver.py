import scraper
import csv
import os.path
from time import localtime, strftime

data_foldername = "data"

romeo_datafile = "./data/romeo_data.csv"
romeo_data_header = ["datetime", "temperature", "electric conductivity", "pH"]

golf_datafile = "./data/golf_data.csv"
golf_data_header = ["datetime", "co2content", "temperature"]

# Check if folder exits
if not os.path.exists(f"./{data_foldername}"):
    os.makedirs(data_foldername)
    print(
        f"[{strftime('%Y-%m-%d %H:%M:%S', localtime())}] Created Directory {data_foldername}"
    )

# Prozess
exising_data = scraper.get_raw_measurements_data()
splitted_rows = [b.split() for b in exising_data]
splitted_rows.reverse()

romeo_data = [
    [f"{row[0]} {row[1]}"] + row[2 : len(romeo_data_header) + 1]
    for row in splitted_rows
]
golf_data = [
    [f"{row[len(romeo_data_header) + 1]} {row[len(romeo_data_header)+2]}"]
    + row[1 - len(golf_data_header) :]
    for row in splitted_rows
    if len(row) > len(romeo_data_header) + 1
]


# Save Data
with open(romeo_datafile, "w", newline="") as csvfile:
    filewriter = csv.writer(
        csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    filewriter.writerow(romeo_data_header)
    filewriter.writerows(romeo_data)

with open(golf_datafile, "w", newline="") as csvfile:
    filewriter = csv.writer(
        csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    filewriter.writerow(golf_data_header)
    filewriter.writerows(golf_data)

print(f"[{strftime('%Y-%m-%d %H:%M:%S', localtime())}] All measurements saved!")
