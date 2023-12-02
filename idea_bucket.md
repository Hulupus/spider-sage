# Aquaponik Dashboard Scraper 

<!-- V1: Basic Scraper: Return Data to Console      -->
<!-- V1.2: Save Data in CSV                         -->
<!-- V1.3: Reverse given Dataset                    -->
<!-- V2: Merge "date" and "time" column to fix graph-->

Add only new data

def get_new_data(curr_dataset):
    data = get_raw_measurements_data()
    return data[: len(data) - curr_dataset + 1]  # get also last element to compare

print(get_new_data(909))

Output when new files are created:

Check if dataset exists