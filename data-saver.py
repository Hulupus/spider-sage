#
#           data-saver.py
#
#           by Hulupus
#
#           V1: Basic Scraper: Return Data to Console
#           V1.2: Save Data in CSV
#           V1.3: Reverse given Dataset
#
#           V2: Merge "date" and "time" column to fix graph
#
#           V3: Added third dataset to scrape
#           V3.2: Added dynamic dataset scraper
#           V3.3 Outsourced code to seperate scraper class
#           V3.4 Cleanup unnecessary code
#

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
    print(f"Created Directory {data_foldername}")

# Create Scraper
s = scraper.Scraper(
    url="my-data-dashboard",
    output_e="div",
    data_wrapper="p",
)


# Prozess
s.read_raw_measurements_data()
s.split_datarows_into_cells()
s.flip_data()
s.split_data_in_datasets(datasets)


# Save Data
data = s.get_data()
for i, dataset in enumerate(datasets):
    with open(f"./{data_foldername}/{dataset[0]}_data.csv", "w", newline="") as csvfile:
        filewriter = csv.writer(
            csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        filewriter.writerow(dataset[1])
        filewriter.writerows(data[i])
    print(f"{len(data[i])} measurements from {dataset[0]} saved!")
