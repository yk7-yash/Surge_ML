# Q.3 URL Shortener
from __future__ import with_statement

import sys
from os import path
import csv
import webbrowser
import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' +
                   urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def main():
    field_names = ['Original URL', 'Short URL']
    print("\n1.Short a URL\n2.Enter a short URL to search and browse")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        url = input("Enter a URL to short: ")
        shrt_url = make_tiny(url)
        print(shrt_url)

        # Store URL and Short URL in a CSV File
        current_dir = path.dirname(__file__)
        filename = path.join(current_dir, "URL.csv")
        data = {'Original URL': url, 'Short URL': shrt_url}
        with open(filename, "a") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
            csv_writer.writerow(data)

    elif (choice == 2):
        shrt_url = input("Enter the Short URL to browse: ")

        # Check in CSV File for Short URL provided
        with open("URL.csv", 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=field_names)
            visited = 'no'
            for row in csv_reader:
                if (shrt_url == row["Short URL"]):
                    webbrowser.open(row["Original URL"])
                    visited = 'yes'
            if (visited != 'yes'):
                print("The Short URL provided does not exist")


if __name__ == '__main__':
    main()