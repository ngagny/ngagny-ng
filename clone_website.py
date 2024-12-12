import os
import requests
from bs4 import BeautifulSoup

def download_page(url, folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open(os.path.join(folder, 'index.html'), 'w') as file:
        file.write(soup.prettify())

def main():
    url = input("Enter the URL of the website to clone: ")
    folder = url.split('//')[-1].split('/')[0]
    if not os.path.exists(folder):
        os.makedirs(folder)
    download_page(url, folder)
    print(f"Website cloned into folder: {folder}")

if __name__ == "__main__":
    main()
