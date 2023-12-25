# Data Scraper
# Author: Mike van Veen
# Last Change: 25.12.23

from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, url, outputstream, data_element) -> None:
        self.data = []
        self.url = url
        self.outputstream = outputstream
        self.data_element = data_element

    def read_raw_measurements_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        div = soup.find(self.outputstream, attrs={"class": "raw_data_outputstream"})
        measurements = div.find_all(self.data_element)
        self.data = [meas.get_text().strip() for meas in measurements]

    def split_datarows_into_cells(self):
        self.data = [row.split() for row in self.data]

    def flip_data(self):
        self.data.reverse()

    def split_data_in_datasets(self, datasets):
        data = []
        biases = [0] * len(self.data)
        for i, dataset in enumerate(datasets):
            rows = []
            for j, row in enumerate(self.data):
                x = [i for i, value in enumerate(row) if "-" in value] + [len(row)]
                if (
                    i + biases[j] + 1 >= len(x)
                    or x[i + biases[j] + 1] - x[i + biases[j]] != len(dataset[1]) + 1
                ):
                    biases[j] -= 1
                    continue
                rows.append(
                    [f"{row[x[i + biases[j]]]} {row[x[i + biases[j]] + 1]}"]
                    + row[x[i + biases[j]] + 2 : x[i + biases[j] + 1]]
                )

            data.append(rows)
        self.data = data

    def get_data(self):
        return self.data


if __name__ == "__main__":
    print("Hello")
