from bs4 import BeautifulSoup
import requests

URL = "https://schillersigfox.sytes.net:45201/cgi-bin/dashboardROMEO.cgi"


def get_raw_measurements_data():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    div = soup.find("div", attrs={"class": "raw_data_outputstream"})
    measurements = div.find_all("p")
    return [meas.get_text().strip() for meas in measurements]


if __name__ == "__main__":
    print(len(get_raw_measurements_data()))
    print(get_raw_measurements_data()[0].split(" "), sep="\n")
