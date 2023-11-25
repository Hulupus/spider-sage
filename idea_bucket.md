# Scraper 

Add only new data

def get_new_data(curr_dataset):
    data = get_raw_measurements_data()
    return data[: len(data) - curr_dataset + 1]  # get also last element to compare

print(get_new_data(909))

# Saver

Output when new files are created:

#Check if dataset exists