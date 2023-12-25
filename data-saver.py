# Data Saver
# Author: Mike van Veen
# Last Change: 25.12.23

import scraper
import csv
import os.path


# Define Datasets and Datafolder
datasets = [
    ("romeo", ["datetime", "temperature", "electric conductivity", "pH"]),
    ("golf", ["datetime", "co2content", "temperature"]),
    ("papa", ["datetime", "co2content", "temperature"]),
]

data_foldername = "data"
if not os.path.exists(f"./{data_foldername}"):
    os.makedirs(data_foldername)
    print(f"[Created Directory {data_foldername}")

# Create Scraper
s = scraper.Scraper(
    url="https://schillersigfox.sytes.net:45201/cgi-bin/dashboardROMEO.cgi",
    outputstream="div",
    data_element="p",
)


# Prozess
s.read_raw_measurements_data()
s.split_datarows_into_cells()
s.flip_data()
s.split_data_in_datasets(datasets=datasets)


# Save Data
data = s.get_data()
for i, dataset in enumerate(datasets):
    with open(f"./{data_foldername}/{dataset[0]}_data.csv", "w", newline="") as csvfile:
        filewriter = csv.writer(
            csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        filewriter.writerow(dataset[1])
        filewriter.writerows(data[i])
    print(f"All measurements from {dataset[0]} saved!")
