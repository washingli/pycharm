# file-name: pdf_download.py
import urllib

__author__ = 'rxread'
import requests
from bs4 import BeautifulSoup


def download_file(url):
    local_filename = url.split('/')[-1]
    print(local_filename)
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    # print(r.text)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

    # http://ww0.java4.datastructures.net/handouts/


root_link = "http://www.facc.com/en/Investor-Relations/Reports"
r = requests.get(root_link)
if r.status_code == 200:
    soup = BeautifulSoup(r.text)
    print(soup.prettify())
    # index = 1
    for link in soup.find_all('a', class_="download download-pdf"):

        new_link = 'http://www.facc.com' + link.get('href')
        print(new_link)
        if new_link.endswith(".pdf"):
            file_path = download_file(new_link)
            print("downloading:" + new_link + " -> " + file_path)
            # index += 1
    print("all download finished")
else:
    print("errors occur.")
