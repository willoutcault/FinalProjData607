import urllib.request
from selenium import webdriver
import time
import os


def get_taxi_urls(driver, url):
    all_urls = []

    print('Initiating driver.')
    driver.get(url)
    time.sleep(3)

    print('Iterating through urls.')
    for a in driver.find_elements_by_xpath('.//a'):
        all_urls.append(a.get_attribute('href'))

    time.sleep(3)
    print('Closing driver.')
    driver.close()
    return all_urls


def download_taxi_files(url, path):

    try:
        if url.split('/', 5)[4].endswith('.csv'):
            file_name = url.split('/', 5)[4]
            print(f'Downloading {file_name}.')
            urllib.request.urlretrieve(url, os.path.join(path, file_name))

        else:
            file_name = url.split('/', 5)[5]
            print(f'Downloading {file_name}.')
            urllib.request.urlretrieve(url, os.path.join(path, url.split('/', 5)[5]))

    except Exception as e:
        print(e)


def main():
    driver = webdriver.Chrome()
    taxi_url = 'https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
    taxi_urls = []
    yellow_taxi_urls = []
    green_taxi_urls = []
    fhv_taxi_urls = []

    yellow_taxi_path = os.path.abspath('Yellow_Raw_Files')
    green_taxi_path = os.path.abspath('Green_Raw_Files')
    fhv_taxi_path = os.path.abspath('FHV_Raw_Files')

    all_urls = get_taxi_urls(driver, taxi_url)

    for url in all_urls:
        if 'yellow_tripdata' in url:
            yellow_taxi_urls.append(url)
            taxi_urls.append(url)

        elif 'green_tripdata' in url:
            green_taxi_urls.append(url)
            taxi_urls.append(url)

        elif 'fhv_tripdata' in url:
            fhv_taxi_urls.append(url)
            taxi_urls.append(url)

    print(f'There are {len(yellow_taxi_urls)} yellow taxi urls available. \n', yellow_taxi_urls)
    print(f'There are {len(green_taxi_urls)} yellow taxi urls available. \n', green_taxi_urls)
    print(f'There are {len(fhv_taxi_urls)} yellow taxi urls available. \n', fhv_taxi_urls)

    for url in yellow_taxi_urls:
        download_taxi_files(url, yellow_taxi_path)

    for url in green_taxi_urls:
        download_taxi_files(url, green_taxi_path)

    for url in fhv_taxi_urls:
        download_taxi_files((url, fhv_taxi_path))


if __name__ == '__main__':
    main()